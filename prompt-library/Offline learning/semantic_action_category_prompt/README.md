# `semantic_action_category_prompt`

- Stage: `pre_scene_action_parsing`
- Agent or module: `LLMTemplateActionCategoryModule`
- Role: assigns an `action_category` to each induced action template. The current code only allows `manipulation` or `active_observation`.
- Main inputs: `instruction` and example-augmented `action_templates`.
- Main outputs: an `action_categories` list, where each item includes at least `canonical_action_name` and `action_category`.
- Related artifacts: not written directly as a standalone output; the result flows into later `action_taxonomy.jsonl` rows and the template registry.
- Note: downstream passive, init, and active observation learning all depend on these action categories.
