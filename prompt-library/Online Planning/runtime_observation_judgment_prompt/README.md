# `runtime_observation_judgment_prompt`

Agent: `RuntimeObservationJudgmentAgent`

Used by:
- `run_interactive_executor.py (observation path)`

Role:
Judges the truth values of applicable observation literals from sampled execution frames during online interaction.

Trigger condition:
Used by the runtime observation step inside `run_interactive_executor.py` when there are applicable observables for the current action outcome.

Major inputs:
- domain_summary
- instruction
- objects
- action_context including action name, effect bucket, success, variant rank, and action arguments
- applicable_observables
- image_time_order_note
- camera_order_top_to_bottom and image_layout_note when available
- sampled execution frame images

Major outputs:
- JSON field `observable_judgments`
- each row contains `observable_literal`, `observable_value`, optional `confidence`, and optional `justification`
- converted into `RuntimeObservationJudgmentResult` with true/false observable lists

Code path:
- `run_interactive_executor.py` -> `RuntimeObservationJudgmentAgent.judge_observations()`
