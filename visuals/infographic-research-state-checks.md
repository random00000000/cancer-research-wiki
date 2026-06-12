# Infographic Research State Checks

Status: active review log
Last updated: 2026-06-12

This log periodically compares the current Goal 1 infographic against what the wiki now knows. The goal is to keep the visual honest as research deepens, without overloading the public-facing infographic.

Current canonical image: `visuals/cancer-literacy-infographic.svg`

Current translated support: `i18n/INFOGRAPHIC_CAPTIONS.md`

Current safety add-on visual: `visuals/cancer-claim-filter.svg`

Current localized claim-filter variants:

- Spanish: `visuals/cancer-claim-filter.es.svg`
- German: `visuals/cancer-claim-filter.de.svg`
- Mandarin Chinese: `visuals/cancer-claim-filter.zh.svg`
- Russian: `visuals/cancer-claim-filter.ru.svg`

Current companion mechanism visual: `visuals/cancer-keeps-adapting.svg`

Current screening/vaccination decision visual: `visuals/screening-vaccination-decision.svg`

Current infection-related cancer prevention visual: `visuals/infection-prevention-cancer.svg`

Current environment/work prevention visual: `visuals/environment-work-cancer-prevention.svg`

Current site-specific prevention visual: `visuals/site-specific-prevention-levers.svg`

Current relative versus absolute risk visual: `visuals/relative-vs-absolute-risk.svg`

Current population burden/no-blame visual: `visuals/population-burden-not-blame.svg`

Current agent-facing risk mechanism map: `visuals/risk-mechanism-prevention-map.svg`

Current localized site-specific prevention variants:

- Spanish: `visuals/site-specific-prevention-levers.es.svg`
- German: `visuals/site-specific-prevention-levers.de.svg`
- Mandarin Chinese: `visuals/site-specific-prevention-levers.zh.svg`
- Russian: `visuals/site-specific-prevention-levers.ru.svg`

Current localized population burden/no-blame variants:

- Spanish: `visuals/population-burden-not-blame.es.svg`
- German: `visuals/population-burden-not-blame.de.svg`
- Mandarin Chinese: `visuals/population-burden-not-blame.zh.svg`
- Russian: `visuals/population-burden-not-blame.ru.svg`

Current localized screening/vaccination decision variants:

- Spanish: `visuals/screening-vaccination-decision.es.svg`
- German: `visuals/screening-vaccination-decision.de.svg`
- Mandarin Chinese: `visuals/screening-vaccination-decision.zh.svg`
- Russian: `visuals/screening-vaccination-decision.ru.svg`

Current localized infection-prevention variants:

- Spanish: `visuals/infection-prevention-cancer.es.svg`
- German: `visuals/infection-prevention-cancer.de.svg`
- Mandarin Chinese: `visuals/infection-prevention-cancer.zh.svg`
- Russian: `visuals/infection-prevention-cancer.ru.svg`

Current localized environment/work variants:

- Spanish: `visuals/environment-work-cancer-prevention.es.svg`
- German: `visuals/environment-work-cancer-prevention.de.svg`
- Mandarin Chinese: `visuals/environment-work-cancer-prevention.zh.svg`
- Russian: `visuals/environment-work-cancer-prevention.ru.svg`

Current localized relative/absolute risk variants:

- Spanish: `visuals/relative-vs-absolute-risk.es.svg`
- German: `visuals/relative-vs-absolute-risk.de.svg`
- Mandarin Chinese: `visuals/relative-vs-absolute-risk.zh.svg`
- Russian: `visuals/relative-vs-absolute-risk.ru.svg`

Current localized companion mechanism variants:

- Spanish: `visuals/cancer-keeps-adapting.es.svg`
- German: `visuals/cancer-keeps-adapting.de.svg`
- Mandarin Chinese: `visuals/cancer-keeps-adapting.zh.svg`
- Russian: `visuals/cancer-keeps-adapting.ru.svg`

Current visual QA log: `visuals/visual-qa-log.md`

## 2026-06-12 Check: Headless Chrome Render QA

New QA artifacts:

- `tools/render_svg_contact_sheets.py`
- `visuals/qa-renders/svg-browser-render-qa-report.md`
- `visuals/qa-renders/contact-sheets/contact-sheet-01.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-02.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-03.png`
- `visuals/qa-renders/contact-sheets/contact-sheet-04.png`

### What Changed

- The current SVG set now has repeatable headless Chrome render QA in addition to XML structural QA.
- All 56 current SVGs render to nonblank PNGs at their declared canvas sizes.
- Contact sheets make it easier to inspect the visual set across languages and companions without opening every SVG one by one.
- The claim-filter localized variants were included in this render pass; obvious German and Russian text overflow found during contact-sheet/full-size inspection was corrected before commit.
- The infection-prevention visual set was included in the latest render pass; obvious English template overflow was corrected before commit, and English, German, Russian, and Mandarin full-size previews were inspected.
- The environment/work visual set was included in the latest render pass; English, German, Russian, and Mandarin full-size previews were inspected, and obvious Russian card overflow was corrected before commit.

### Decision For The Flagship Infographic

Do not mark the visual set final yet. The render pass proves the files are not blank in Chrome, but close layout review and native/expert translation review are still needed before treating localized medical visuals as publication-ready.

## 2026-06-12 Check: Population Burden Is Not Personal Blame Visual

New visual:

- `visuals/population-burden-not-blame.svg`
- `visuals/population-burden-not-blame.es.svg`
- `visuals/population-burden-not-blame.de.svg`
- `visuals/population-burden-not-blame.zh.svg`
- `visuals/population-burden-not-blame.ru.svg`

### What Changed

- The wiki now has a public visual separating population-attributable burden from individual causation or moral blame.
- The visual uses peer-reviewed/global-burden source anchors already tracked in `prevention/effect-size-evidence.md`, `prevention/lifestyle-and-burden-evidence.md`, and `prevention/non-screening-absolute-risk-examples.md`.
- It highlights global risk-attributable cancer deaths, U.S. evaluated modifiable-risk-attributable cases, and infection-attributable cases while emphasizing systems: policy, access, housing, food, vaccines, screening follow-up, work safety, and support.
- First-pass localized versions now exist for Spanish, German, Mandarin Chinese, and Russian.

### Decision For The Flagship Infographic

Keep the flagship infographic's no-blame sentence short. Use this companion when readers need a stronger explanation of why population prevention matters without implying that cancer patients caused their disease.

### Translation Impact

Keep the localized no-blame visual under native review before promotion. The translations must preserve that population-attributable burden is a planning model and prevention opportunity, not a personal-causation or moral-blame claim.

## 2026-06-12 Check: Infection-Related Cancer Prevention Visual

Evidence page:

- `prevention/infection-related-cancer-prevention.md`

New visual:

- `visuals/infection-prevention-cancer.svg`
- `visuals/infection-prevention-cancer.es.svg`
- `visuals/infection-prevention-cancer.de.svg`
- `visuals/infection-prevention-cancer.zh.svg`
- `visuals/infection-prevention-cancer.ru.svg`

### What Changed

- The wiki now has a public companion visual explaining that cancer is not contagious like a cold, but persistent infections can raise risk through chronic damage, inflammation, viral genes, and tissue change.
- The visual highlights HPV, HBV/HCV, and H. pylori because the current evidence page already tracks strong non-CDC-heavy anchors: Lancet Global Health infection-attributable burden, NEJM HPV cohort evidence, England HPV programme impact, Taiwan HBV vaccination data, HCV cure cohorts, and H. pylori eradication meta-analyses.
- First-pass localized versions now exist for Spanish, German, Mandarin Chinese, and Russian.

### Decision For The Flagship Infographic

Keep the flagship infographic's vaccine/screening wording broad. Use this companion when readers need to understand why infection prevention is a root-cause cancer prevention pathway, not merely a lifestyle tip.

### Translation Impact

Keep localized infection-prevention visuals under native review before promotion. Vaccine, screening, pathogen, and stigma-related wording varies by country and language, and should avoid implying that cancer itself is casually contagious.

## 2026-06-12 Check: Environment And Work Prevention Visual

Evidence page:

- `prevention/environmental-exposure-evidence.md`

New visual:

- `visuals/environment-work-cancer-prevention.svg`
- `visuals/environment-work-cancer-prevention.es.svg`
- `visuals/environment-work-cancer-prevention.de.svg`
- `visuals/environment-work-cancer-prevention.zh.svg`
- `visuals/environment-work-cancer-prevention.ru.svg`

### What Changed

- The wiki now has a public companion visual showing that cancer prevention is also clean air, safe buildings, worker protection, remediation, and fair policy.
- The visual highlights radon, asbestos, PM2.5 air pollution, and workplace carcinogen controls using the existing environmental evidence page, which tracks meta-analyses and specialist reviews rather than relying on CDC-only public summaries.
- First-pass localized versions now exist for Spanish, German, Mandarin Chinese, and Russian.

### Decision For The Flagship Infographic

Keep the flagship infographic's structural-exposure message short. Use this companion when readers need a concrete explanation of why cancer prevention includes environmental and occupational controls, not only personal choices.

### Translation Impact

Keep localized environment/work visuals under native review before promotion. Radon, asbestos, PM2.5, remediation, and worker-safety terms vary by region and legal system.

## 2026-06-12 Check: Relative Versus Absolute Risk Visual

New visual:

- `visuals/relative-vs-absolute-risk.svg`
- `visuals/relative-vs-absolute-risk.es.svg`
- `visuals/relative-vs-absolute-risk.de.svg`
- `visuals/relative-vs-absolute-risk.zh.svg`
- `visuals/relative-vs-absolute-risk.ru.svg`

### What Changed

- The wiki now has a public risk-communication visual explaining why a relative-risk percentage needs a baseline, denominator, time horizon, and absolute difference.
- The visual uses an explicitly illustrative example so it does not invent a universal cancer effect size.
- It also separates population prevention from personal blame, matching `prevention/risk-communication.md` and the population-attributable fraction cautions in `prevention/effect-size-evidence.md`.
- First-pass localized versions now exist for Spanish, German, Mandarin Chinese, and Russian.

### Decision For The Flagship Infographic

Keep the flagship infographic's short risk-reduction caveat. Use this companion when a reader or agent needs to interpret percentages, headlines, screening claims, prevention claims, or population-attributable burden.

### Translation Impact

Keep the translated risk visual conservative until native review. The localized versions preserve the English caveats: illustrative example, baseline risk, time horizon, uncertainty, and no personal blame.

## 2026-06-12 Check: Site-Specific Prevention Levers

New visual:

- `visuals/site-specific-prevention-levers.svg`
- `visuals/site-specific-prevention-levers.es.svg`
- `visuals/site-specific-prevention-levers.de.svg`
- `visuals/site-specific-prevention-levers.zh.svg`
- `visuals/site-specific-prevention-levers.ru.svg`

### What Changed

- The wiki now has a public companion visual mapping major cancer sites to the highest-signal prevention, vaccination, screening, and exposure-reduction levers.
- The visual comes from `prevention/cancer-site-prevention-map.md` and keeps site-specific caveats visible instead of implying that one generic lifestyle rule fits every cancer.
- It avoids date-sensitive screening age cutoffs and keeps personal risk, symptoms, inherited risk, cancer history, and local guidance inside the clinician-involvement boundary.
- First-pass localized versions now exist for Spanish, German, Mandarin Chinese, and Russian.

### Decision For The Flagship Infographic

Do not cram cancer-site details into the flagship public infographic. Keep the flagship broad, and use this companion visual when readers need to understand why prevention advice differs for colorectal, cervical, liver, lung, skin, breast, stomach, and oral/oropharyngeal cancers.

### Translation Impact

Keep the localized site-specific prevention visual under native review before promotion. The translations must preserve the caveat that this is a map for questions, not personal screening, vaccination, or treatment advice.

## 2026-06-12 Check: Cancer Headline Reading Guide

New evidence page:

- `prevention/how-to-read-cancer-headlines.md`

### What Changed

- The wiki now has a public and agent-facing guide for interpreting cancer "breakthrough" stories, viral protocols, clinical-trial headlines, and early research claims.
- The guide adds an evidence ladder, red-flag headline patterns, safer question rewrites, and source cards on health-news exaggeration and cancer misinformation.
- This supports the claim-filter visual without overcrowding the flagship cancer literacy infographic.

### Decision For The Flagship Infographic

Do not add headline-reading rules to the flagship infographic. Keep the flagship image focused on what cancer is and how risk can be reduced, and keep headline evaluation in the claim-filter/headline-reading companion material.

## 2026-06-12 Check: Screening And Vaccination Decision Visual

New visual:

- `visuals/screening-vaccination-decision.svg`
- `visuals/screening-vaccination-decision.es.svg`
- `visuals/screening-vaccination-decision.de.svg`
- `visuals/screening-vaccination-decision.zh.svg`
- `visuals/screening-vaccination-decision.ru.svg`

### What Changed

- The wiki now has a public visual that separates symptoms from screening and shows that screening/vaccination decisions depend on age, anatomy, risk, local guidance, benefits, harms, and follow-up access.
- The visual avoids date-sensitive age cutoffs and points readers toward clinician-guided decisions rather than personal medical instructions.
- It uses the existing screening, screening-harms, and infection-prevention evidence pages as its source backbone.
- First-pass localized variants now exist for Spanish, German, Mandarin Chinese, and Russian.

### Decision For The Flagship Infographic

Keep the flagship infographic's broad wording about recommended screening and vaccination. Use the new decision visual as the companion when readers need the benefit-harm and personalization logic.

## 2026-06-12 Check: Risk Mechanism Prevention Map

New visual:

- `visuals/risk-mechanism-prevention-map.svg`

### What Changed

- The wiki now has an agent-facing concept map linking risk inputs, mechanisms, cancer capabilities, and prevention levers.
- The visual is designed to support specialist-style answers by forcing an explicit chain: claim, exposure/input, mechanism, cancer behavior/site, evidence strength, lever, and caveat.
- The map is intentionally denser than the public infographic and should not replace the first everyday-human visual.

### Decision For The Flagship Infographic

Keep the flagship infographic simple. Use this map for agent retrieval, internal reasoning, and future visual planning rather than embedding the full mechanism chain into the public image.

## 2026-06-12 Check: Visual QA Baseline

New QA page:

- `visuals/visual-qa-log.md`

### What Changed

- The current SVG set now has a structural QA record covering XML parsing, `width`, `height`, `viewBox`, `<title>`, and `<desc>` checks.
- Browser rendering was attempted through a temporary local server, but the in-app browser blocked the direct render route through client security policy.
- The QA log therefore distinguishes proven structural validity from still-needed browser screenshot QA and translation review.

### Decision For The Flagship Infographic

Do not mark the visual work as finished yet. The README can keep embedding the current flagship and companion images, but future completion requires browser or renderer screenshots that prove text does not clip and non-Latin glyphs render acceptably.

Current localized image variants:

- Spanish: `visuals/cancer-literacy-infographic.es.svg`
- German: `visuals/cancer-literacy-infographic.de.svg`
- Mandarin Chinese: `visuals/cancer-literacy-infographic.zh.svg`
- Russian: `visuals/cancer-literacy-infographic.ru.svg`
- French: `visuals/cancer-literacy-infographic.fr.svg`
- Portuguese: `visuals/cancer-literacy-infographic.pt.svg`
- Arabic: `visuals/cancer-literacy-infographic.ar.svg`
- Hindi: `visuals/cancer-literacy-infographic.hi.svg`
- Japanese: `visuals/cancer-literacy-infographic.ja.svg`
- Korean: `visuals/cancer-literacy-infographic.ko.svg`
- Italian: `visuals/cancer-literacy-infographic.it.svg`
- Turkish: `visuals/cancer-literacy-infographic.tr.svg`
- Indonesian: `visuals/cancer-literacy-infographic.id.svg`
- Vietnamese: `visuals/cancer-literacy-infographic.vi.svg`

## 2026-06-12 Check: Growth Mechanism Map

New evidence page:

- `concepts/cancer-growth-mechanism-map.md`

New companion visual:

- `visuals/cancer-keeps-adapting.svg`
- `visuals/cancer-keeps-adapting.es.svg`
- `visuals/cancer-keeps-adapting.de.svg`
- `visuals/cancer-keeps-adapting.zh.svg`
- `visuals/cancer-keeps-adapting.ru.svg`

### What Changed

- The wiki now separates cancer growth into five retrieval layers: cell instructions, cell behavior, evolution, ecosystem, and spread.
- The mechanism map strengthens the infographic's "how cancer keeps growing" claim with hallmarks, clonal evolution, tumor microenvironment, immune escape, and metastasis-colonization source cards.
- The source mix is primarily peer-reviewed literature and conceptual reviews rather than CDC-style public-health summaries.
- The companion SVG turns the deeper map into a public visual without overloading the flagship README infographic.

### Decision For The Flagship Infographic

The current flagship infographic is still acceptable as a first-pass public visual. It already shows normal control breaking down, changes accumulating, cancer behavior, a growth loop, and spread.

Do not add the full mechanism map to the flagship image. The next visual should be a companion infographic called "How cancer keeps adapting," with:

- A visible selection-pressure loop.
- A tumor ecosystem ring around cancer cells.
- A metastasis obstacle-course strip that makes clear most disseminated cells fail.

### Translation Impact

First-pass companion translations now exist for Spanish, German, Mandarin Chinese, and Russian. Future work should visually QA these and expand to the remaining flagship languages only after checking text fit and translation safety.

## 2026-06-12 Check: Claim Filter Evidence Add-On

New evidence page:

- `prevention/cancer-claim-filter.md`

New visual:

- `visuals/cancer-claim-filter.svg`
- `visuals/cancer-claim-filter.es.svg`
- `visuals/cancer-claim-filter.de.svg`
- `visuals/cancer-claim-filter.zh.svg`
- `visuals/cancer-claim-filter.ru.svg`

### What Changed

- The wiki now has a reusable five-gate public filter for cancer claims: human outcomes, absolute impact, replication, harms/interactions, and care delay.
- New claim cards cover alkaline diets, detoxes, supplements, high-dose vitamin C, cannabis/cannabinoids, ivermectin/fenbendazole, fasting, and ketogenic diets.
- The new page uses non-CDC-heavy sources, including AICR/WCRF, ASCO, systematic reviews, peer-reviewed trials, and frontier-review caution around drug repurposing.
- First-pass localized claim-filter variants now exist for Spanish, German, Mandarin Chinese, and Russian.

### Decision For The Flagship Infographic

Do not add the claim cards to the flagship cancer literacy infographic. The flagship image should stay focused on what cancer is, how it grows, and high-confidence risk levers.

Instead:

- Keep `visuals/cancer-claim-filter.svg` as a separate public safety visual.
- Link the claim-filter page from the README research backing.
- Keep localized claim-filter visuals under native review before public-final use, because misleading claims often use local idioms and culture-specific fear hooks.

### Translation Impact

The localized claim-filter visuals are useful for access, but they are also higher-risk than neutral mechanism diagrams. Future crawl passes should collect language-specific examples of misleading cancer prevention and treatment claims so translations can be tuned to real public-risk wording without amplifying scams.

## 2026-06-12 Check: Translated Infographic Assets

New assets:

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

### What Changed

- The project now has actual localized SVG infographics for Spanish, German, Mandarin Chinese, Russian, French, Portuguese, Arabic, Hindi, Japanese, Korean, Italian, Turkish, Indonesian, and Vietnamese, not only translated captions.
- The localized variants keep the same core evidence message as the English first-pass infographic: cancer is a loss of normal cell-control systems, risk can be reduced but not eliminated, and prevention is not blame.
- The localized variants use shorter text than the canonical English SVG so translated labels fit better.

### Remaining Gap

- The originally planned localized image set is now represented. Remaining work is visual QA, translation review, and future language expansion.
- The localized SVGs should eventually receive visual QA in a browser or renderer to catch font fallback, clipping, and line-overflow issues.
- Future ALDH2/flushing visual add-ons should be localized separately rather than squeezed into the flagship image.

## 2026-06-12 Check: Alcohol, ALDH2, Tobacco, And Upper Aerodigestive Risk

New evidence pages:

- `prevention/alcohol-and-cancer-evidence.md`
- `prevention/alcohol-aldh2-tobacco-upper-aerodigestive-evidence.md`

### What The Current Infographic Already Handles

- It includes alcohol as a risk-reduction lever.
- It frames risk reduction as probability change, not a guarantee.
- It avoids blame and avoids claiming cancer is fully controllable.

### What The Current Infographic Does Not Yet Show

- Alcohol risk is partly mechanistic through acetaldehyde and DNA damage.
- ALDH2 low-activity variants can make acetaldehyde clearance slower; facial flushing after alcohol can be a warning sign.
- Alcohol and tobacco together are especially important for upper aerodigestive cancers.
- Some risk messages need localized wording for East Asian audiences without stereotyping.

### Decision For The Flagship Infographic

Do not add ALDH2 genotype details to the main body of the first flagship infographic yet. It would make the public visual too dense and could create ethnic stereotyping if compressed into one icon or sentence.

Instead:

- Keep the main infographic line as "limit or avoid alcohol."
- Consider adding a small optional footnote in a future version: "Alcohol risk can be higher for some people because of biology, dose, and tobacco co-exposure."
- Make a separate localized add-on visual for alcohol flushing/ALDH2, especially for Mandarin, Japanese, and Korean translation tracks.
- Make a separate claim-filter or risk-lever visual explaining "same exposure, different biology."

### Translation Impact

The translated caption set should stay aligned with the canonical infographic for now. Future localized variants should include:

- Mandarin, Japanese, and Korean wording about alcohol flushing that avoids shame and avoids using ancestry as destiny.
- Clear wording that facial flushing is not a diagnosis.
- Clear wording that tobacco avoidance remains important across populations.

### Next Visual Tasks

- Add a localized visual brief for "alcohol flushing is a warning sign, not a badge."
- Add icons or visual notes for "dose", "biology", and "combined exposures" in the next risk-reduction visual.
- Update `i18n/INFOGRAPHIC_CAPTIONS.md` when the canonical SVG text changes or when localized image variants are created.
