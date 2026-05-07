# `goal_state_satisfaction_prompt`

Agent: `GoalInferenceAgent`

Used by:
- `generate_online_problem.py`

Role:
Checks whether one enumerated grounded goal assignment really satisfies the task instruction.

Trigger condition:
Used once for every enumerated candidate goal assignment after mutex filtering and semantic pruning.

Major inputs:
- goal-focused domain_summary
- instruction
- objects
- assignment_id
- grounded_goal_relevant_assignment
- assignment_conjunction_pddl

Major outputs:
- JSON fields `satisfies_instruction` and optional `rationale`
- used to keep only satisfying goal states in the final online problem goal expression

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `GoalInferenceAgent`
