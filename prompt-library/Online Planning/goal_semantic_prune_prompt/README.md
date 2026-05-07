# `goal_semantic_prune_prompt`

Agent: `GoalInferenceAgent`

Used by:
- `generate_online_problem.py`

Role:
Removes semantically invalid grounded goal predicates before assignment enumeration.

Trigger condition:
Used after grounded goal candidates and mutex groups are assembled.

Major inputs:
- goal-focused domain_summary
- instruction
- objects
- candidate_grounded_predicates
- selected_mutex_groups

Major outputs:
- JSON field `pruned_grounded_predicates`
- used to filter the grounded-goal candidate set and any mutex groups

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `GoalInferenceAgent`
