# `goal_relevant_ground_atoms_prompt`

Agent: `GoalInferenceAgent`

Used by:
- `generate_online_problem.py`

Role:
Selects the grounded predicates that are plausible goal atoms for the current instruction.

Trigger condition:
Used after goal-relevant predicate schemas have been selected.

Major inputs:
- goal-focused domain_summary
- instruction
- objects
- goal_relevant_predicates
- candidate_grounded_predicates

Major outputs:
- JSON field `goal_relevant_grounded_predicates`
- validated into a unique ordered list of grounded `Predicate` objects

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `GoalInferenceAgent`
