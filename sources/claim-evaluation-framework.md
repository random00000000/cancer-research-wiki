# Cancer Claim Evaluation Framework

Status: first-pass agent framework
Last updated: 2026-06-12

This page helps agents evaluate cancer prevention and cancer biology claims without relying on institutional branding or internet popularity.

## Core Rule

Evidence is not the same as confidence.

A claim may be biologically plausible, emotionally compelling, heavily marketed, or repeated by experts, yet still be too weak for public guidance. Agents should separate:

- Mechanistic plausibility.
- Observational association.
- Human intervention evidence.
- Effect size.
- Absolute risk.
- Harms.
- Cost and opportunity cost.
- Whether the claim delays proven prevention, screening, diagnosis, or treatment.

## Claim Triage

When a claim appears, classify it:

1. Established
   - Supported by multiple high-quality human studies, coherent mechanism, consistent findings, and credible expert synthesis.
   - Example: tobacco increases cancer risk.

2. Probable
   - Strong but not perfect human evidence, supported by mechanism and consistency.
   - Example: healthy dietary patterns and physical activity lower risk for several cancers.

3. Plausible but unproven
   - Mechanistically interesting or observationally associated, but intervention evidence is weak, indirect, or absent.
   - Example: many specific "anti-cancer" nutrients.

4. Preliminary
   - Early cell, animal, preprint, small trial, or biomarker evidence.
   - Must not become public guidance without caveats.

5. Misleading
   - Overstates evidence, ignores harms, confuses association with causation, or implies certainty without adequate data.

6. Dangerous
   - Encourages replacing or delaying proven prevention, screening, diagnosis, or treatment.

## Evidence Questions

Ask:

- What exactly is the claim?
- Is it about cancer incidence, mortality, recurrence, symptoms, biomarkers, tumor shrinkage, or quality of life?
- Is the evidence from humans, animals, cells, or models?
- Was the outcome clinically meaningful or only a surrogate marker?
- How large is the effect in absolute terms?
- Is there dose-response evidence?
- Is there replication across independent groups?
- Are confounding and reverse causation plausible?
- Does the mechanism match the human outcome?
- Who benefits, who is harmed, and who was studied?
- What is the opportunity cost?
- Is someone selling a product, ideology, or protocol?

## Causal Reasoning Tools

Use Bradford Hill-style viewpoints as prompts, not a checklist:

- Strength of association.
- Consistency.
- Temporality.
- Dose-response.
- Biological plausibility.
- Coherence with other evidence.
- Experimental evidence where available.
- Analogy to known mechanisms.

Use GRADE-style thinking:

- Certainty can be downgraded for risk of bias, inconsistency, indirectness, imprecision, and publication bias.
- Certainty can be upgraded when effects are large, dose-response is clear, and confounding would likely reduce rather than inflate an effect.

Use NCI PDQ-style screening/prevention caution:

- Prevention and screening claims need both benefit and harm assessment.
- Relative risk is not enough; absolute risk matters.

## Red-Flag Language

Treat claims as suspicious when they use:

- "Doctors do not want you to know."
- "Kills cancer cells" without human outcome data.
- "Detoxes cancer."
- "Boosts immunity" as a cure or prevention guarantee.
- "Starves cancer."
- "Natural chemotherapy."
- "Cancer cannot survive in an alkaline body."
- "Proven in the lab" used as if it proves human benefit.
- "No side effects."
- "Works for all cancers."
- Testimonials instead of controlled evidence.

## Public Response Template

For questionable claims, answer like this:

1. Direct classification: established, probable, plausible but unproven, preliminary, misleading, or dangerous.
2. What evidence exists.
3. What evidence is missing.
4. Known or plausible harms.
5. Better-supported alternatives.
6. Medical safety boundary if the claim touches diagnosis or treatment.

## Source Cards

### GRADE Handbook

- URL: https://gradepro.org/handbook/
- Source type: evidence certainty framework
- Reusable claims:
  - GRADE provides a structured process for rating certainty of evidence and developing recommendations.
- Caution:
  - GRADE is a framework; applying it well requires domain expertise.

### Bradford Hill Causality Viewpoints Review

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206235/
- Source type: epidemiology review
- Reusable claims:
  - Bradford Hill viewpoints are commonly used to assess causal inference in epidemiology.
- Caution:
  - Hill viewpoints are not a mechanical checklist and do not prove causation by themselves.

### NCI PDQ Levels of Evidence for Screening and Prevention

- URL: https://www.cancer.gov/publications/pdq/levels-evidence/screening-prevention
- Source type: cancer prevention/screening evidence framework
- Reusable claims:
  - NCI PDQ distinguishes solid, fair, and inadequate evidence for health effects of screening and prevention interventions.
  - Benefit and harm estimates both matter.
- Caution:
  - Use as a framework, not as the only authority.

## Wiki Implication

Every major prevention claim should eventually have a claim card with:

- Claim text.
- Evidence class.
- Best sources.
- Human outcome data.
- Mechanism.
- Effect size.
- Harms.
- Confidence.
- Verdict.
