# `init_observable_judgment_prompt`

Agent: `PerPredicateInitBeliefAgent`

Used by:
- `generate_online_problem.py`

Role:
Judges the truth value of an observable from the initial scene image so the uncertain initial belief can be calibrated from visual evidence.

Trigger condition:
Used only in the observation-aware initialization branch, once a grounded predicate has been matched to an observation-module observable.

Major inputs:
- domain_summary
- instruction
- image_input_note
- objects
- manipulation_records
- target_observable
- target_predicate
- scene image

Major outputs:
- JSON field `observable_value` with `true` or `false`
- used to collapse or update uncertain initial-belief factors

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `PerPredicateInitBeliefAgent`
