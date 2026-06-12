# Visual QA Log

Status: active
Last updated: 2026-06-12

This log records practical visual and accessibility checks for Goal 1 SVG assets. XML validity is not the same as human visual quality, so this file separates what has been verified from what still needs browser or native-language review.

## 2026-06-12 Structural SVG QA

Scope:

- Flagship cancer literacy infographic: English plus localized SVGs.
- Companion adaptation infographic: English plus first localized SVGs.
- Claim-filter add-on visual.

Checked files:

- `visuals/cancer-literacy-infographic.svg`
- `visuals/cancer-literacy-infographic.es.svg`
- `visuals/cancer-literacy-infographic.de.svg`
- `visuals/cancer-literacy-infographic.zh.svg`
- `visuals/cancer-literacy-infographic.ru.svg`
- `visuals/cancer-literacy-infographic.fr.svg`
- `visuals/cancer-literacy-infographic.pt.svg`
- `visuals/cancer-literacy-infographic.ar.svg`
- `visuals/cancer-literacy-infographic.hi.svg`
- `visuals/cancer-literacy-infographic.ja.svg`
- `visuals/cancer-literacy-infographic.ko.svg`
- `visuals/cancer-literacy-infographic.it.svg`
- `visuals/cancer-literacy-infographic.tr.svg`
- `visuals/cancer-literacy-infographic.id.svg`
- `visuals/cancer-literacy-infographic.vi.svg`
- `visuals/cancer-keeps-adapting.svg`
- `visuals/cancer-keeps-adapting.es.svg`
- `visuals/cancer-keeps-adapting.de.svg`
- `visuals/cancer-keeps-adapting.zh.svg`
- `visuals/cancer-keeps-adapting.ru.svg`
- `visuals/screening-vaccination-decision.svg`
- `visuals/screening-vaccination-decision.es.svg`
- `visuals/screening-vaccination-decision.de.svg`
- `visuals/screening-vaccination-decision.zh.svg`
- `visuals/screening-vaccination-decision.ru.svg`
- `visuals/risk-mechanism-prevention-map.svg`
- `visuals/site-specific-prevention-levers.svg`
- `visuals/relative-vs-absolute-risk.svg`
- `visuals/population-burden-not-blame.svg`
- `visuals/cancer-claim-filter.svg`

Result:

- All checked SVG files parse as XML.
- All checked SVG files expose explicit `width`, `height`, and `viewBox` attributes.
- All checked SVG files include a `<title>` element.
- All checked SVG files include a `<desc>` element.
- Root README links the canonical flagship infographic, companion adaptation visual, localized flagship variants, and first localized companion variants.
- `i18n/README.md`, `visuals/README.md`, and `visuals/infographic-research-state-checks.md` index the current localized SVG sets.

Browser QA attempt:

- A temporary local server was started on `127.0.0.1:8765` for browser-based rendering checks.
- The in-app browser refused direct `data:` and localhost SVG render checks because of client URL/security policy.
- The temporary server was stopped after the blocked attempt.
- Because browser rendering was blocked, this pass does not prove absence of text clipping, font fallback issues, or cross-browser layout problems.

## Current Visual QA Status

| Asset group | Structural QA | Browser screenshot QA | Translation review |
| --- | --- | --- | --- |
| Flagship English SVG | Passed | Still needed | Not applicable |
| Flagship localized SVGs | Passed | Still needed | Still needed |
| Companion adaptation English SVG | Passed | Still needed | Not applicable |
| Companion adaptation localized SVGs | Passed | Still needed | Still needed |
| Screening/vaccination decision English SVG | Passed | Still needed | Not applicable |
| Screening/vaccination decision localized SVGs | Passed | Still needed | Still needed |
| Risk/mechanism/prevention agent map | Passed | Still needed | Not applicable |
| Site-specific prevention levers SVG | Passed | Still needed | Not applicable |
| Relative versus absolute risk SVG | Passed | Still needed | Not applicable |
| Population burden/no-blame SVG | Passed | Still needed | Not applicable |
| Claim-filter SVG | Passed | Still needed | Not applicable |

## Next Visual QA Tasks

- Render all SVGs in a normal browser outside the blocked in-app route and inspect for clipping, overflow, unreadable text, missing glyphs, and layout imbalance.
- Prioritize visual QA for Mandarin Chinese, Arabic, Hindi, Japanese, Korean, Russian, and Vietnamese because font fallback and glyph shaping risks are higher.
- Add native or expert translation review before treating any localized medical wording as final.
- If browser QA finds clipping, shorten localized labels before expanding companion visuals to the remaining languages.
