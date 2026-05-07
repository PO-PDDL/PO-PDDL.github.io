# `init_object_location_judgment_prompt`

Agent: `PerPredicateInitBeliefAgent`

Used by:
- `generate_online_problem.py`

Role:
Jointly judges all candidate location predicates for one target movable object.

Trigger condition:
Used after location predicates are identified and grouped by object.

Major inputs:
- domain_summary
- instruction
- image_input_note
- objects
- target_object
- fixed_location_predicates from historical priors when available
- candidate_location_predicates
- manipulation_records
- scene image

Major outputs:
- JSON field `predicate_judgments`
- each row contains `predicate`, `truth_value`, and optional `justification`
- converted into per-predicate `PredicateTruthJudgment` results

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `PerPredicateInitBeliefAgent`
