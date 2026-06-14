# Sequencing And Biomarker Decision Checklist

Status: first-pass tool
Last updated: 2026-06-14

Audience label: patient question preparation, clinician discussion support, research support, not medical advice.

## Purpose

The Rosie-style path depends on data. In humans, the question is not "sequence everything immediately." The question is: what decision-grade biomarker or genomic data could change a legitimate next step?

## Ask The Oncology Team

- What biomarker tests are standard for this cancer type and stage?
- Has the tumor already had next-generation sequencing?
- Was testing tissue-based, blood-based ctDNA, germline, RNA, immunohistochemistry, FISH, PCR, or another method?
- Was matched normal testing done?
- Is germline genetic testing relevant?
- Is the current tissue sample sufficient and recent enough?
- Would repeat biopsy be safe and useful?
- Would RNA expression, HLA typing, TMB, MSI/MMR, PD-L1, HRD, or fusion testing matter?
- Could biomarker results qualify the patient for approved therapy, off-label review, clinical trials, cell therapy, TCR therapy, or mRNA/neoantigen trials?

## Data Types And Why They Matter

| Data type | What it may reveal | Limits |
| --- | --- | --- |
| Pathology and IHC | Cancer type, subtype, receptors, mismatch repair, PD-L1, lineage markers. | May not capture all genomic drivers. |
| Tumor DNA NGS | Mutations, copy number changes, fusions, tumor mutational burden, some signatures. | Needs sufficient tumor; not every alteration is actionable. |
| Matched normal DNA | Distinguishes inherited variants from tumor-specific mutations. | Adds consent and interpretation complexity. |
| Germline testing | Inherited cancer-risk or treatment-relevant variants. | Has family implications and needs counseling. |
| RNA sequencing | Expression, fusions, transcript evidence. | Less routinely available; quality depends on tissue. |
| HLA typing | Antigen presentation context for TCR/neoantigen strategies. | Necessary for some trials, not a treatment by itself. |
| ctDNA | Blood-based tumor DNA signal, sometimes resistance or minimal residual disease. | False negatives happen; context matters. |
| Repeat biopsy | Current tumor state after resistance. | Invasive and only worthwhile if it can change action. |

## mRNA / Neoantigen-Specific Questions

- Is there a legitimate trial for this cancer type and stage?
- Does the trial require tumor-normal sequencing?
- Does it require HLA typing?
- Does it require fresh biopsy or archival tissue?
- Does it require RNA expression data?
- What is the manufacturing timeline?
- What happens if too few usable neoantigens are found?
- What combination therapy is used?
- What endpoints and toxicities are tracked?

## Sources

- NCI biomarker testing for cancer treatment: https://www.cancer.gov/about-cancer/treatment/types/biomarker-testing-cancer-treatment
- NCI-MATCH precision medicine background: https://www.cancer.gov/about-cancer/treatment/clinical-trials/nci-supported/nci-match
- `../mrna/mrna-cancer-therapy-pathway.md`
- `../mrna/manufacturing-constraints.md`
- `../mrna/clinical-endpoints-and-evidence-labels.md`

## Safety Boundary

This checklist helps ask whether testing is useful. It does not tell anyone to order, interpret, or act on sequencing without a qualified clinical team.
