# Cancer Case Packet Builder

Status: first-pass tool
Last updated: 2026-06-14

Audience label: patient question preparation, advanced-options navigation, clinician discussion support, not medical advice.

## Purpose

The case packet turns a human cancer situation into a reviewable object. Without this packet, expert outreach becomes vague and trial teams cannot judge eligibility.

## One-Page Case Summary Template

```text
Patient initials or alias:
Age:
Country/state:
Cancer type and subtype:
Stage:
Date diagnosed:
Current disease status:
Current treating oncologist / institution:

Pathology:
- Biopsy/surgery date:
- Primary site:
- Histology:
- Grade:
- Margins/nodes if surgical:
- Pathology report attached? yes/no

Imaging:
- Latest CT/MRI/PET date:
- Sites of disease:
- Measurable lesions:
- Imaging reports attached? yes/no
- Actual image files available? yes/no

Biomarkers and genomics:
- Standard biomarkers:
- Tumor NGS:
- Germline testing:
- RNA expression:
- HLA typing:
- ctDNA:
- Reports attached? yes/no

Prior treatments:
- Surgery:
- Radiation:
- Chemotherapy:
- Immunotherapy:
- Targeted therapy:
- Hormonal therapy:
- Cell therapy:
- Trials:
- Best response and reason stopped:

Current clinical status:
- Symptoms:
- Performance status if known:
- Major comorbidities:
- Organ-function concerns:
- Urgent risks:

Question for experts:
- What advanced legitimate options should be reviewed now?
```

## Required Attachments

- Pathology report.
- Molecular/biomarker reports.
- Imaging reports.
- Actual scan images if possible.
- Oncology notes.
- Treatment timeline.
- Medication list.
- Lab trend.
- Discharge summaries and operative/radiation reports if relevant.

## Missing-Data Checklist

- Exact diagnosis unclear.
- Stage unclear.
- No recent scan.
- No biomarker testing despite cancer type where biomarkers commonly guide therapy.
- Sequencing done but report not available.
- Progression suspected but not documented.
- Prior treatment response not summarized.
- No statement of current treatment intent.

## AI Use

Safe AI tasks:

- Convert records into a dated timeline.
- Extract biomarkers and prior therapies.
- Draft questions for the oncologist.
- Generate a missing-records checklist.
- Summarize papers and trials with citations.

Unsafe AI tasks:

- Choosing treatment.
- Designing a vaccine or drug.
- Recommending dose or schedule.
- Telling a patient to delay, combine, stop, or start therapy.

## Output

The output should be a clean packet for:

- Treating oncologist.
- Second-opinion cancer center.
- Molecular tumor board.
- Trial office.
- Expanded-access discussion.
- Researcher outreach when appropriate.
