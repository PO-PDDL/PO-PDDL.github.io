# `init_deterministic_grouping_prompt`

Agent: `PerPredicateInitBeliefAgent`

Used by:
- `generate_online_problem.py`

Role:
Finds exactly-one deterministic groups and picks the single true predicate inside each group.

Trigger condition:
Used in deterministic initialization after individual predicate judgments are available.

Major inputs:
- domain_summary
- instruction
- image_input_note
- objects
- manipulation_records
- deterministic_ground_predicates with truth values and justifications
- scene image

Major outputs:
- JSON field `exactly_one_groups`
- each group may include `name`, `predicates`, `selected_true_predicate`, and `description`
- used to repair deterministic judgments for mutually exclusive groups

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `PerPredicateInitBeliefAgent`
