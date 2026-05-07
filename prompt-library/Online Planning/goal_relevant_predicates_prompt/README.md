# `goal_relevant_predicates_prompt`

Agent: `GoalInferenceAgent`

Used by:
- `generate_online_problem.py`

Role:
Selects which predicate schemas are relevant to the natural-language goal instruction.

Trigger condition:
Used when `generate_online_problem.py` does not reuse an existing problem file.

Major inputs:
- goal-focused domain_summary
- instruction
- objects
- candidate_predicates with signatures and parameter types

Major outputs:
- JSON field `goal_relevant_predicates`
- validated into an ordered list of predicate-schema names

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `GoalInferenceAgent`
