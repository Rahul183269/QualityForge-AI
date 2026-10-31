# QualityForge AI - Version Tracking

## Objective
Make every AI evaluation run traceable and reproducible.

## Version Registry

| Component | Current Version | Description |
|---|---|---|
| AI Model / Provider | rule-based-v1 | Deterministic local prototype; no external LLM |
| Prompt | prompt-v1 | Initial structured prompt specification |
| Evaluation Dataset | dataset-v1 | test_data/ai_evaluation_cases.json |
| Evaluation Logic | evaluator-v1 | scripts/evaluate_ai_summaries.py |

## Versioning Rules

1. Increment the model version when the analysis implementation or provider changes.
2. Increment the prompt version whenever prompt instructions or output requirements change.
3. Increment the dataset version when evaluation cases are added, removed, or modified.
4. Increment the evaluation version when evaluation logic or pass criteria change.

## Evaluation Run Traceability

Every evaluation run should record:

- Run ID
- Execution timestamp
- Model/provider version
- Prompt version
- Dataset version
- Evaluation logic version
- Total cases
- Passed cases
- Failed cases
- Regression gate result

## Current Prototype Limitations

- The current summarizer is rule-based, not an external LLM.
- No external model provider or model API version is configured.
- Prompt version identifies the documented prompt specification; it does not mean an LLM prompt is currently executed.
- Versions are manually maintained at this stage.

## Definition of Done

- [x] Model/provider version documented.
- [x] Prompt version documented.
- [x] Evaluation dataset version documented.
- [x] Evaluation logic version documented.
- [x] Versioning and traceability rules defined.
