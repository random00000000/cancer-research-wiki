# mRNA Cancer Trial Tracker

Status: starter registry tracker
Last updated: 2026-06-14

Audience label: trial landscape review, patient question preparation, research intelligence, not for clinical use.

This tracker starts with registry fields checked from ClinicalTrials.gov on 2026-06-14. Registry status can change, so future agents must refresh these rows during later crawls.

## Registry Snapshot

| NCT | Product / platform | Cancer type | Phase | Status on 2026-06-14 | Enrollment | Primary endpoint | Evidence reading |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| NCT03897881 | mRNA-4157/V940 + pembrolizumab | High-risk melanoma | Phase 2 | Active, not recruiting | 267 | Recurrence-free survival | Published randomized phase 2b anchor; still investigational |
| NCT05933577 | Intismeran autogene/V940 + pembrolizumab | High-risk melanoma | Phase 3 | Active, not recruiting | 1089 | Recurrence-free survival | Practice-changing question; phase 3 confirmation needed |
| NCT06961006 | Intismeran autogene/V940 + pembrolizumab | Advanced melanoma | Phase 2 | Recruiting | 160 | Progression-free survival | Tests advanced melanoma setting, not adjuvant recurrence |
| NCT06077760 | Intismeran autogene/V940 + pembrolizumab | Non-small cell lung cancer | Phase 3 | Recruiting | 868 | Disease-free survival | Tests whether melanoma signal travels to NSCLC |
| NCT06623422 | Pembrolizumab with or without V940 | Non-small cell lung cancer | Phase 3 | Recruiting | 680 | Disease-free survival | Additional NSCLC phase 3 frontier |
| NCT07221474 | V940/placebo + pembrolizumab + chemotherapy | Metastatic squamous NSCLC | Phase 2 | Recruiting | 180 | Progression-free survival and overall survival | First-line metastatic squamous NSCLC frontier |
| NCT06295809 | Intismeran autogene/V940 + pembrolizumab | Cutaneous squamous cell carcinoma | Phase 2/3 | Terminated | 46 | Event-free survival | Important negative/uncertain signal; sponsor page says enrollment stopped and no phase 3 expansion |
| NCT06307431 | Intismeran autogene/V940 + pembrolizumab | Renal cell carcinoma | Phase 2 | Active, not recruiting | 272 | Disease-free survival | Disease-specific immune biology question |
| NCT06305767 | Intismeran autogene/V940 + pembrolizumab | Bladder cancer | Phase 1/2 | Active, not recruiting | 230 | DFS and adverse-event endpoints by cohort | Safety and recurrence-setting question |
| NCT06833073 | Intismeran autogene/V940 + BCG | High-risk non-muscle-invasive bladder cancer | Phase 2 | Recruiting | 308 | Event-free survival | Tests V940 with BCG, not pembrolizumab |
| NCT05968326 | Autogene cevumeran + atezolizumab + mFOLFIRINOX | Resected pancreatic ductal adenocarcinoma | Phase 2 | Recruiting | 260 | Disease-free survival | Tests early PDAC immune signal in randomized setting |
| NCT04486378 | RO7198457/autogene cevumeran versus watchful waiting | ctDNA-positive resected colorectal cancer | Phase 2 | Active, not recruiting | 327 | Disease-free survival | Minimal residual disease / ctDNA-positive frontier |
| NCT04526899 | BNT111 and cemiplimab combinations | Advanced melanoma | Phase 2 | Completed | 184 | Objective response rate | Shared-antigen FixVac signal; peer-reviewed full details needed |
| NCT02316457 | Individualized neoantigen mRNA-lipoplex vaccine | Triple-negative breast cancer | Phase 1 | Completed | See publication | Safety, tolerability, and immune response | Small 2026 Nature immune-durability report; not definitive efficacy |

## How To Read This Tracker

- "Recruiting" or "active" is not evidence that a therapy works.
- "Terminated" is scientifically important and should be crawled for reasons, not ignored.
- Enrollment count is not the same as number of people who received a personalized product.
- Endpoints differ: recurrence-free survival, disease-free survival, event-free survival, objective response rate, toxicity, and immune response answer different questions.
- A registry row is not a publication; always link trial records to peer-reviewed papers, conference abstracts, and sponsor updates when available.

## Fields To Add Next

- Sponsor and collaborator.
- Disease stage and setting.
- Adjuvant, neoadjuvant, metastatic, minimal residual disease, or recurrent setting.
- Personalized neoantigen versus shared antigen.
- Delivery platform.
- Combination therapy.
- Manufacturing success rate and median turnaround time.
- Toxicity summary and discontinuation.
- Publication status.
- Last checked date and source URL for each row.

## Current Interpretation Labels

- Moderate investigational evidence: KEYNOTE-942 in resected high-risk melanoma because it is randomized and uses recurrence-free survival, but still needs phase 3 confirmation and regulatory review.
- Low-to-preliminary clinical-benefit evidence but important immune biology: autogene cevumeran in PDAC and individualized TNBC vaccine reports.
- Preliminary sponsor-reported evidence: BNT111 phase 2 topline advanced melanoma and company-reported V940 five-year updates until full peer-reviewed details are available.
- Negative/uncertain evidence to track: terminated cSCC V940 program and any trial with incomplete enrollment, discontinued development, or missing results.
