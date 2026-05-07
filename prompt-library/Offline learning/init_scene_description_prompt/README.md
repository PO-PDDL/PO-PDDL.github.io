# `init_scene_description_prompt`

- Stage: `scene_description`
- Agent or module: `InitSceneDescriptionGenerator`
- Role: generates the initial English scene description for `step_000_init` from the episode's first frame.
- Main inputs: `instruction`, the future action sequence, `allowed_object_names`, the initial frame image, and optional `camera_order_top_to_bottom`.
- Main outputs: a JSON response containing a parseable `scene_description_text`; the code materializes this as `InitSceneDescriptionGenerationResult`.
- Related artifacts: `init_scene_description.txt`, `init_scene_description_generation.json`, and an updated `step 0 observation_text` in `annotated_episode.json`.
- Note: this is a VLM prompt, and the system prompt additionally stresses that only visually supported allowed objects may be described.
