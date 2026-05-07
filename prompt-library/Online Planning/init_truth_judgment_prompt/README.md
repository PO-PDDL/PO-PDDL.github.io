# `init_truth_judgment_prompt`

Agent: `PerPredicateInitBeliefAgent`

Used by:
- `generate_online_problem.py`

Role:
Judges whether one grounded predicate is true or false in the initial online-planning scene.

Trigger condition:
Used in the deterministic initialization branch for standalone grounded predicates that are not handled by rule defaults or grouped location repair.

Major inputs:
- domain_summary
- instruction
- image_input_note
- objects
- target_predicate
- manipulation_records
- scene image

Major outputs:
- JSON fields `truth_value` and optional `justification`
- parsed into one `PredicateTruthJudgment`

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `PerPredicateInitBeliefAgent`
