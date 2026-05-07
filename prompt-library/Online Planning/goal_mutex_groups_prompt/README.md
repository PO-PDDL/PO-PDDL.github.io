# `goal_mutex_groups_prompt`

Agent: `GoalInferenceAgent`

Used by:
- `generate_online_problem.py`

Role:
Identifies groups of grounded goal predicates that should be mutually exclusive during goal enumeration.

Trigger condition:
Used when at least two grounded goal predicates remain after selection.

Major inputs:
- goal-focused domain_summary
- instruction
- objects
- candidate_mutex_group_predicates

Major outputs:
- JSON field `mutex_groups`
- each group is a list of grounded predicate strings
- validated into non-overlapping mutex groups

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `GoalInferenceAgent`
