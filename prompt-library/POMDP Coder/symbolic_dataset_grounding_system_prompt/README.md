# `symbolic_dataset_grounding_system_prompt`

Stage: `2_symbolic_dataset_grounding`

Role:
Converts one annotated episode into symbolic transition records aligned with the induced task interface.

Trigger condition:
Used once per episode in Stage 2 when grounding demonstrations into a symbolic dataset.

Major inputs:
- task_name
- task_spec from Stage 1
- one annotated episode payload

Major outputs:
- one JSON object with key `records`
- each record includes state_t, action_t, action_outcome_t, observation_t, state_t_plus_1, reward_t, terminal_t, and metadata
- validated and written into split JSONL datasets

Runtime assembly note:
This prompt is defined inline in the stage module rather than stored as a standalone prompt file in the upstream repository.
