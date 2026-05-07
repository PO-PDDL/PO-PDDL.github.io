# `passive_observation_vlm_confirmation_prompt`

- Stage: `passive_observation_learning`
- Agent or module: `VLMContradictionConfirmationModuleLLM`
- Role: visually confirms whether the suspected passive-observation contradictions are real.
- Main inputs: `record`, `filtered_state_before`, `candidate_ground_truth_facts`, `suspects`, `predicate_comments`, and the current step `frame_paths`.
- Main outputs: `confirmed_contradictions` and `summary`.
- Related artifacts: contributes to passive-observation evidence aggregation and influences final observation-rule statistics and module generation.
- Note: for stacked multi-camera images, the code automatically prefixes `camera_order_top_to_bottom` to the user prompt.
