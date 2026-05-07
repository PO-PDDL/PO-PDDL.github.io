# `active_observation_vlm_confirmation_prompt`

- Stage: `active_observation_learning`
- Agent or module: `VLMActiveObservationValueConfirmationModule`
- Role: visually confirms the true values of the predicates targeted by an active-observation step.
- Main inputs: `record`, `filtered_current_state`, `candidate_ground_truth_facts`, `targets`, `predicate_comments`, and the current step `frame_paths`.
- Main outputs: `confirmed_observations` and `summary`.
- Related artifacts: contributes to `active_observation_evidence.jsonl` and affects `active_observation_module.pddl`.
- Note: this is the visual confirmation step in the active-observation learning path.
