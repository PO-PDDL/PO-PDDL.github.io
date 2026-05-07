# `init_uncertain_grouping_prompt`

Agent: `PerPredicateInitBeliefAgent`

Used by:
- `generate_online_problem.py`

Role:
Groups uncertain predicates into binary, mutex, or correlated belief factors before observation-aware calibration.

Trigger condition:
Used only when the domain has an observation module and `--skip-init-observation` is not set.

Major inputs:
- domain_summary
- instruction
- image_input_note
- objects
- manipulation_records
- uncertain_ground_predicates
- scene image

Major outputs:
- JSON field `groups`
- each group includes `name`, `group_kind`, `predicates`, and optional descriptive fields
- validated into belief-factor grouping metadata

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `PerPredicateInitBeliefAgent`
