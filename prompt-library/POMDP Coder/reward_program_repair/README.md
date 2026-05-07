# `reward_program_repair`

Stage: `6_program_repair_loop`

Role:
Repairs the reward model.

Trigger condition:
Used in Stage 6 to repair failed `reward` candidates using mismatch payloads from evaluation.

Major inputs:
- base repair prompt text
- execution_rules.md
- reward_program_spec.md
- shared_api_context.json
- current failed program
- sanitized mismatch payload from evaluation

Major outputs:
- a full updated Python program
- keeps the same function signature
- stored as repaired candidate code plus prompt/response artifacts

Runtime assembly note:
The pipeline does not send this file alone. It prepends/appends execution rules, component spec, shared API context, the current failed program, and mismatch evidence to build the final repair prompt.
