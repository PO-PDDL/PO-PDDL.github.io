# `init_location_predicates_prompt`

Agent: `PerPredicateInitBeliefAgent`

Used by:
- `generate_online_problem.py`

Role:
Selects which predicate schemas should be treated as location predicates and therefore grouped by movable object for joint judging.

Trigger condition:
Used during deterministic initial-state inference before object-wise location judging.

Major inputs:
- domain_summary
- candidate_predicates with predicate names and parameter types

Major outputs:
- JSON field `location_predicates`
- validated as a set of predicate-schema names

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `PerPredicateInitBeliefAgent`
