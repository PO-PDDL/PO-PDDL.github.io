# `active_observation_discovery_prompt`

- Stage: `active_observation_learning`
- Agent or module: `LLMActiveObservationDiscoveryModule`
- Role: identifies which predicates an `active_observation` action actually inspected and what values it observed.
- Main inputs: `record`, `filtered_current_state`, `candidate_ground_truth_facts`, `predicate_comments`, `feature_predicate_names`, and `available_observables`.
- Main outputs: `discovered_observations` and `summary`.
- Related artifacts: contributes to `active_observation_evidence.jsonl` and `active_observation_rule_statistics.json`.
- Note: the code requires this prompt to discover at least one observation target for each active-observation step.
