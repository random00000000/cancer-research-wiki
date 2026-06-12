# Visual QA Log

Status: active
Last updated: 2026-06-12

This log records practical visual and accessibility checks for Goal 1 SVG assets. XML validity is not the same as human visual quality, so this file separates what has been verified from what still needs browser or native-language review.

## 2026-06-12 Structural SVG QA

Scope:

- Flagship cancer literacy infographic: English plus localized SVGs.
- Companion adaptation infographic: English plus first localized SVGs.
- Claim-filter add-on visual: English plus first localized SVGs.
- Infection-prevention add-on visual: English plus first localized SVGs.
- Environment/work add-on visual: English plus first localized SVGs.
- Alcohol biology add-on visual: English plus first localized SVGs.
- Tobacco cessation add-on visual: English plus first localized SVGs.
- Metabolic health add-on visual: English plus first localized SVGs.
- UV/sun add-on visual: English plus first localized SVGs.
- Vaccine-preventable cancer add-on visual: English plus first localized SVGs.
- Radon/home add-on visual: English plus first localized SVGs.

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
- `visuals/site-specific-prevention-levers.es.svg`
- `visuals/site-specific-prevention-levers.de.svg`
- `visuals/site-specific-prevention-levers.zh.svg`
- `visuals/site-specific-prevention-levers.ru.svg`
- `visuals/relative-vs-absolute-risk.svg`
- `visuals/relative-vs-absolute-risk.es.svg`
- `visuals/relative-vs-absolute-risk.de.svg`
- `visuals/relative-vs-absolute-risk.zh.svg`
- `visuals/relative-vs-absolute-risk.ru.svg`
- `visuals/population-burden-not-blame.svg`
- `visuals/population-burden-not-blame.es.svg`
- `visuals/population-burden-not-blame.de.svg`
- `visuals/population-burden-not-blame.zh.svg`
- `visuals/population-burden-not-blame.ru.svg`
- `visuals/cancer-claim-filter.svg`
- `visuals/cancer-claim-filter.es.svg`
- `visuals/cancer-claim-filter.de.svg`
- `visuals/cancer-claim-filter.zh.svg`
- `visuals/cancer-claim-filter.ru.svg`
- `visuals/infection-prevention-cancer.svg`
- `visuals/infection-prevention-cancer.es.svg`
- `visuals/infection-prevention-cancer.de.svg`
- `visuals/infection-prevention-cancer.zh.svg`
- `visuals/infection-prevention-cancer.ru.svg`
- `visuals/environment-work-cancer-prevention.svg`
- `visuals/environment-work-cancer-prevention.es.svg`
- `visuals/environment-work-cancer-prevention.de.svg`
- `visuals/environment-work-cancer-prevention.zh.svg`
- `visuals/environment-work-cancer-prevention.ru.svg`
- `visuals/alcohol-aldh2-tobacco-risk.svg`
- `visuals/alcohol-aldh2-tobacco-risk.es.svg`
- `visuals/alcohol-aldh2-tobacco-risk.de.svg`
- `visuals/alcohol-aldh2-tobacco-risk.zh.svg`
- `visuals/alcohol-aldh2-tobacco-risk.ru.svg`
- `visuals/tobacco-cessation-cancer-risk.svg`
- `visuals/tobacco-cessation-cancer-risk.es.svg`
- `visuals/tobacco-cessation-cancer-risk.de.svg`
- `visuals/tobacco-cessation-cancer-risk.zh.svg`
- `visuals/tobacco-cessation-cancer-risk.ru.svg`
- `visuals/metabolic-health-cancer-prevention.svg`
- `visuals/metabolic-health-cancer-prevention.es.svg`
- `visuals/metabolic-health-cancer-prevention.de.svg`
- `visuals/metabolic-health-cancer-prevention.zh.svg`
- `visuals/metabolic-health-cancer-prevention.ru.svg`
- `visuals/uv-sun-tanning-cancer-prevention.svg`
- `visuals/uv-sun-tanning-cancer-prevention.es.svg`
- `visuals/uv-sun-tanning-cancer-prevention.de.svg`
- `visuals/uv-sun-tanning-cancer-prevention.zh.svg`
- `visuals/uv-sun-tanning-cancer-prevention.ru.svg`
- `visuals/vaccine-preventable-cancers.svg`
- `visuals/vaccine-preventable-cancers.es.svg`
- `visuals/vaccine-preventable-cancers.de.svg`
- `visuals/vaccine-preventable-cancers.zh.svg`
- `visuals/vaccine-preventable-cancers.ru.svg`
- `visuals/radon-home-lung-cancer-prevention.svg`
- `visuals/radon-home-lung-cancer-prevention.es.svg`
- `visuals/radon-home-lung-cancer-prevention.de.svg`
- `visuals/radon-home-lung-cancer-prevention.zh.svg`
- `visuals/radon-home-lung-cancer-prevention.ru.svg`

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

## 2026-06-12 Headless Chrome Render QA

Scope:

- All 86 SVG files in `visuals/`.

Tooling:

- `tools/render_svg_contact_sheets.py`
- Local renderer: `C:\Program Files\Google\Chrome\Application\chrome.exe`

Generated artifacts:

- `visuals/qa-renders/svg-browser-render-qa-report.md`
- `visuals/qa-renders/contact-sheets/contact-sheet-01.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-02.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-03.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-04.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-05.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-06.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-07.png`

Result:

- Headless Chrome rendered all 86 SVG files at their declared canvas sizes.
- All 86 renders were nonblank.
- Contact-sheet inspection did not reveal blank canvases or completely missing non-Latin glyph rendering.
- Some dense translated visuals, especially non-Latin and right-to-left layouts, still need close human inspection for clipping, text crowding, line overflow, and translation quality.
- The alcohol biology visual set was included in the latest render pass; English, Spanish, Russian, and Mandarin full-size previews were inspected, and obvious safety-panel/footer overflow was corrected before commit.
- The tobacco cessation visual set was included in the latest render pass; English, German, Russian, and Mandarin full-size previews were inspected, and obvious English/German/Russian text overflow was corrected before commit.
- The metabolic health visual set was included in the latest render pass; English, Spanish, German, Russian, and Mandarin full-size previews were inspected, and obvious Spanish/German/Russian overflow was corrected before commit.
- The UV/sun visual set was included in the latest render pass; English, Spanish, German, Russian, and Mandarin full-size previews were inspected.
- The vaccine-preventable cancer visual set was included in the latest render pass; English, Spanish, German, Russian, and Mandarin full-size previews were inspected, and obvious German card overflow was corrected before commit.
- The radon/home visual set was included in the latest render pass; English, Spanish, German, Russian, and Mandarin full-size previews were inspected before commit.

Repository note:

- Full-size intermediate PNG renders are reproducible and ignored at `visuals/qa-renders/png/`.

## Current Visual QA Status

| Asset group | Structural QA | Browser screenshot QA | Translation review |
| --- | --- | --- | --- |
| Flagship English SVG | Passed | Headless Chrome nonblank passed; close layout review still needed | Not applicable |
| Flagship localized SVGs | Passed | Headless Chrome nonblank passed; close layout review still needed | Still needed |
| Companion adaptation English SVG | Passed | Headless Chrome nonblank passed; close layout review still needed | Not applicable |
| Companion adaptation localized SVGs | Passed | Headless Chrome nonblank passed; close layout review still needed | Still needed |
| Screening/vaccination decision English SVG | Passed | Headless Chrome nonblank passed; close layout review still needed | Not applicable |
| Screening/vaccination decision localized SVGs | Passed | Headless Chrome nonblank passed; close layout review still needed | Still needed |
| Risk/mechanism/prevention agent map | Passed | Headless Chrome nonblank passed; close layout review still needed | Not applicable |
| Site-specific prevention levers SVG | Passed | Headless Chrome nonblank passed; close layout review still needed | Not applicable |
| Site-specific prevention levers localized SVGs | Passed | Headless Chrome nonblank passed; close layout review still needed | Still needed |
| Relative versus absolute risk SVG | Passed | Headless Chrome nonblank passed; close layout review still needed | Not applicable |
| Relative versus absolute risk localized SVGs | Passed | Headless Chrome nonblank passed; close layout review still needed | Still needed |
| Population burden/no-blame SVG | Passed | Headless Chrome nonblank passed; close layout review still needed | Not applicable |
| Population burden/no-blame localized SVGs | Passed | Headless Chrome nonblank passed; close layout review still needed | Still needed |
| Claim-filter SVG | Passed | Headless Chrome nonblank passed; close layout review still needed | Not applicable |
| Claim-filter localized SVGs | Passed | Headless Chrome nonblank passed; obvious German/Russian overflow fixed; close layout review still needed | Still needed |
| Infection-prevention SVG | Passed | Headless Chrome nonblank passed; obvious overflow fixed; close layout review still needed | Not applicable |
| Infection-prevention localized SVGs | Passed | Headless Chrome nonblank passed; English/German/Russian/Mandarin full-size previews checked; close layout review still needed | Still needed |
| Environment/work prevention SVG | Passed | Headless Chrome nonblank passed; English full-size preview checked | Not applicable |
| Environment/work prevention localized SVGs | Passed | Headless Chrome nonblank passed; German/Russian/Mandarin full-size previews checked; obvious Russian overflow fixed | Still needed |
| Alcohol biology SVG | Passed | Headless Chrome nonblank passed; English full-size preview checked; safety/footer overflow fixed | Not applicable |
| Alcohol biology localized SVGs | Passed | Headless Chrome nonblank passed; Spanish/Russian/Mandarin full-size previews checked; safety-panel overflow fixed | Still needed |
| Tobacco cessation SVG | Passed | Headless Chrome nonblank passed; English full-size preview checked; heading overflow fixed | Not applicable |
| Tobacco cessation localized SVGs | Passed | Headless Chrome nonblank passed; German/Russian/Mandarin full-size previews checked; German/Russian overflow fixed | Still needed |
| Metabolic health SVG | Passed | Headless Chrome nonblank passed; English full-size preview checked | Not applicable |
| Metabolic health localized SVGs | Passed | Headless Chrome nonblank passed; Spanish/German/Russian/Mandarin full-size previews checked; overflow fixed | Still needed |
| UV/sun SVG | Passed | Headless Chrome nonblank passed; English full-size preview checked | Not applicable |
| UV/sun localized SVGs | Passed | Headless Chrome nonblank passed; Spanish/German/Russian/Mandarin full-size previews checked | Still needed |
| Vaccine-preventable cancer SVG | Passed | Headless Chrome nonblank passed; English full-size preview checked | Not applicable |
| Vaccine-preventable cancer localized SVGs | Passed | Headless Chrome nonblank passed; Spanish/German/Russian/Mandarin full-size previews checked; German overflow fixed | Still needed |
| Radon/home lung cancer SVG | Passed | Headless Chrome nonblank passed; English full-size preview checked | Not applicable |
| Radon/home lung cancer localized SVGs | Passed | Headless Chrome nonblank passed; Spanish/German/Russian/Mandarin full-size previews checked | Still needed |

## Next Visual QA Tasks

- Closely inspect the contact sheets and, where needed, full-size browser renders for clipping, overflow, unreadable text, missing glyphs, and layout imbalance.
- Prioritize visual QA for Mandarin Chinese, Arabic, Hindi, Japanese, Korean, Russian, and Vietnamese because font fallback and glyph shaping risks are higher.
- Add native or expert translation review before treating any localized medical wording as final.
- If browser QA finds clipping, shorten localized labels before expanding companion visuals to the remaining languages.
