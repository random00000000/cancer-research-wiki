# Infographic Research State Checks

Status: active review log
Last updated: 2026-06-12

This log periodically compares the current Goal 1 infographic against what the wiki now knows. The goal is to keep the visual honest as research deepens, without overloading the public-facing infographic.

Current canonical image: `visuals/cancer-literacy-infographic.svg`

Current translated support: `i18n/INFOGRAPHIC_CAPTIONS.md`

Current localized image variants:

- Spanish: `visuals/cancer-literacy-infographic.es.svg`
- German: `visuals/cancer-literacy-infographic.de.svg`
- Mandarin Chinese: `visuals/cancer-literacy-infographic.zh.svg`
- Russian: `visuals/cancer-literacy-infographic.ru.svg`
- French: `visuals/cancer-literacy-infographic.fr.svg`
- Portuguese: `visuals/cancer-literacy-infographic.pt.svg`
- Arabic: `visuals/cancer-literacy-infographic.ar.svg`
- Hindi: `visuals/cancer-literacy-infographic.hi.svg`

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

### What Changed

- The project now has actual localized SVG infographics for Spanish, German, Mandarin Chinese, Russian, French, Portuguese, Arabic, and Hindi, not only translated captions.
- The localized variants keep the same core evidence message as the English first-pass infographic: cancer is a loss of normal cell-control systems, risk can be reduced but not eliminated, and prevention is not blame.
- The localized variants use shorter text than the canonical English SVG so translated labels fit better.

### Remaining Gap

- Japanese, Korean, Italian, Turkish, Indonesian, and Vietnamese still need localized image variants.
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
