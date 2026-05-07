# `task_interface_system_prompt`

Stage: `1_task_interface_induction`

Role:
Induces a reusable symbolic task interface before any model program is proposed.

Trigger condition:
Used once in Stage 1 when the pipeline asks the LLM to design task_spec.json from dataset schema and sampled episodes.

Major inputs:
- task_name
- dataset_schema from Stage 0
- episode_samples from up to six annotated episodes

Major outputs:
- one JSON object representing task_spec
- fields including objects, state_fields, state_schema, action_schemas, observation_schema, goal/reward/terminal interfaces, and executor_interface
- written to task_interface/task_spec.json and summarized into api_summary.md

Runtime assembly note:
This prompt is defined inline in the stage module rather than stored as a standalone prompt file in the upstream repository.
