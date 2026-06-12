"""Render visual SVGs with headless Chrome and build QA contact sheets.

This script is intentionally small and dependency-light. It uses the local
Chrome executable for browser rendering and Pillow for thumbnail sheets.
"""

from __future__ import annotations

import argparse
import math
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageStat


@dataclass
class SvgRender:
    name: str
    width: int
    height: int
    png_path: Path
    nonblank: bool
    brightness_delta: float


def find_chrome(explicit: str | None) -> Path:
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    candidates.extend(
        [
            Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
            Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
            Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
            Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        ]
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise SystemExit("No Chrome or Edge executable found. Pass --chrome PATH.")


def svg_size(svg_path: Path) -> tuple[int, int]:
    root = ET.parse(svg_path).getroot()
    width = root.attrib.get("width")
    height = root.attrib.get("height")
    if not width or not height:
        view_box = root.attrib.get("viewBox", "")
        parts = view_box.split()
        if len(parts) == 4:
            return int(float(parts[2])), int(float(parts[3]))
        raise ValueError(f"{svg_path.name} lacks width/height and usable viewBox")
    return int(float(width)), int(float(height))


def render_svg(chrome: Path, svg_path: Path, png_path: Path, width: int, height: int) -> None:
    png_path.parent.mkdir(parents=True, exist_ok=True)
    output_path = png_path.resolve()
    command = [
        str(chrome),
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--screenshot={output_path}",
        svg_path.resolve().as_uri(),
    ]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not output_path.exists():
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        stdout = result.stdout.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"Chrome did not create {output_path}\nstdout={stdout}\nstderr={stderr}")


def image_nonblank(png_path: Path) -> tuple[bool, float]:
    image = Image.open(png_path).convert("RGB")
    background = Image.new("RGB", image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, background)
    stat = ImageStat.Stat(diff)
    delta = sum(stat.mean) / len(stat.mean)
    return delta > 0.25, delta


def make_contact_sheets(renders: list[SvgRender], out_dir: Path, columns: int, thumb_width: int) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    sheet_paths: list[Path] = []
    rows_per_sheet = 4
    per_sheet = columns * rows_per_sheet
    label_height = 44
    margin = 18
    gap = 16

    for sheet_index in range(math.ceil(len(renders) / per_sheet)):
        chunk = renders[sheet_index * per_sheet : (sheet_index + 1) * per_sheet]
        thumbs: list[tuple[SvgRender, Image.Image]] = []
        cell_height = 0
        for item in chunk:
            image = Image.open(item.png_path).convert("RGB")
            scale = thumb_width / image.width
            thumb_height = max(1, int(image.height * scale))
            thumb = image.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            cell_height = max(cell_height, thumb_height + label_height)
            thumbs.append((item, thumb))

        rows = math.ceil(len(thumbs) / columns)
        sheet_width = margin * 2 + columns * thumb_width + (columns - 1) * gap
        sheet_height = margin * 2 + rows * cell_height + (rows - 1) * gap
        sheet = Image.new("RGB", (sheet_width, sheet_height), "white")
        draw = ImageDraw.Draw(sheet)

        for i, (item, thumb) in enumerate(thumbs):
            row = i // columns
            col = i % columns
            x = margin + col * (thumb_width + gap)
            y = margin + row * (cell_height + gap)
            sheet.paste(thumb, (x, y))
            label_y = y + thumb.height + 6
            draw.text((x, label_y), item.name[:48], fill=(15, 32, 51))
            draw.text((x, label_y + 18), f"{item.width}x{item.height} nonblank={item.nonblank}", fill=(71, 85, 105))

        out_path = out_dir / f"contact-sheet-{sheet_index + 1:02d}.png"
        sheet.save(out_path)
        sheet_paths.append(out_path)

    return sheet_paths


def write_report(report_path: Path, renders: list[SvgRender], sheets: list[Path], chrome: Path) -> None:
    failed = [item for item in renders if not item.nonblank]
    lines = [
        "# SVG Browser Render QA Report",
        "",
        f"Date: {date.today().isoformat()}",
        "",
        f"Renderer: `{chrome}`",
        "",
        f"SVG files rendered: {len(renders)}",
        f"Nonblank renders: {len(renders) - len(failed)}",
        f"Blank or near-blank renders: {len(failed)}",
        "",
        "## Contact Sheets",
        "",
    ]
    lines.extend(f"- `{path.as_posix()}`" for path in sheets)
    lines.extend(
        [
            "",
            "## Limits",
            "",
            "- This confirms headless Chrome can render each SVG to a nonblank PNG at its declared canvas size.",
            "- This does not replace human/browser inspection for clipping, text overflow, font fallback, or translation quality.",
            "- Non-Latin scripts still need native or expert review before promotion.",
            "",
            "## Files",
            "",
            "| SVG | Canvas | Nonblank | Brightness delta |",
            "| --- | ---: | --- | ---: |",
        ]
    )
    for item in renders:
        lines.append(f"| `{item.name}` | {item.width}x{item.height} | {item.nonblank} | {item.brightness_delta:.2f} |")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chrome", help="Path to Chrome or Edge executable")
    parser.add_argument("--visuals", default="visuals", help="Directory containing SVGs")
    parser.add_argument("--out", default="visuals/qa-renders", help="Output directory for PNGs and contact sheets")
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--thumb-width", type=int, default=360)
    args = parser.parse_args()

    chrome = find_chrome(args.chrome)
    visuals_dir = Path(args.visuals)
    out_dir = Path(args.out)
    png_dir = out_dir / "png"
    sheet_dir = out_dir / "contact-sheets"
    report_path = out_dir / "svg-browser-render-qa-report.md"

    renders: list[SvgRender] = []
    for svg_path in sorted(visuals_dir.glob("*.svg")):
        width, height = svg_size(svg_path)
        png_path = png_dir / f"{svg_path.stem}.png"
        render_svg(chrome, svg_path, png_path, width, height)
        nonblank, delta = image_nonblank(png_path)
        renders.append(SvgRender(svg_path.name, width, height, png_path, nonblank, delta))

    sheets = make_contact_sheets(renders, sheet_dir, args.columns, args.thumb_width)
    write_report(report_path, renders, sheets, chrome)

    blank = [item.name for item in renders if not item.nonblank]
    print(f"Rendered {len(renders)} SVGs")
    print(f"Report: {report_path}")
    for path in sheets:
        print(f"Contact sheet: {path}")
    if blank:
        print("Blank or near-blank renders:", ", ".join(blank), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
