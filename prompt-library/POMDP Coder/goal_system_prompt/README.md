# `goal_system_prompt`

Stage: runtime goal parsing

Role:
Translates a natural-language instruction into a machine-checkable goal DSL used by the runtime planner.

Trigger condition:
Used when the runtime bundle is launched with an instruction and `pomdp_coder.runtime.goal.build_goal` asks the LLM to parse that instruction into a structured goal expression.

Major inputs:
- task_name
- instruction
- task_spec

Major outputs:
- one JSON object with `description` and `goal_expr`
- compiled into a runtime goal checker
- stored in runtime goal metadata together with the raw LLM response

Runtime assembly note:
This prompt is defined inline in `pomdp_coder.runtime.goal._build_goal_system_prompt()` rather than stored as a standalone prompt file in the upstream repository.
