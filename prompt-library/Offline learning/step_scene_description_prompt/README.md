# `step_scene_description_prompt`

- Stage: `scene_description`
- Agent or module: `StepSceneDescriptionGenerator`
- Role: generates the English scene description for a later step using sampled frames, prior step descriptions, and current action context.
- Main inputs: `instruction`, `prior_steps`, the current step's `action_text` and `extra_info`, the current frame sequence, the future action sequence, `allowed_object_names`, `current_step_focus_objects`, and optional camera order.
- Main outputs: a JSON response containing `scene_description_text`; the code materializes this as `StepSceneDescriptionGenerationResult`.
- Related artifacts: `step_scene_description.txt`, `step_scene_description_generation.json`, and an updated `observation_text` for the corresponding step in `annotated_episode.json`.
- Note: by default the generator uses only the first and last sampled frames of the step; if the initial response is missing `scene_description_text`, the code automatically retries with a repair suffix.
