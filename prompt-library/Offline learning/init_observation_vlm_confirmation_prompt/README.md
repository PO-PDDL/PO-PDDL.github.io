# `init_observation_vlm_confirmation_prompt`

- Stage: `init_observation_learning`
- Agent or module: `VLMInitContradictionConfirmationModuleLLM`
- Role: visually confirms suspected contradictions for the initial observation using the initial frame images.
- Main inputs: `record`, `filtered_init_facts`, `candidate_ground_truth_facts`, `suspects`, `predicate_comments`, and initial `frame_paths`.
- Main outputs: `confirmed_contradictions` and `summary`.
- Related artifacts: contributes to `init_observation_evidence.jsonl` and affects `init_observation_module.pddl` and related statistics files.
- Note: for stacked multi-camera images, the code automatically prefixes camera-order information into the user prompt.
