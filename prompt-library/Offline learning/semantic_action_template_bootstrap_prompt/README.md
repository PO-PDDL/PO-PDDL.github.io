# `semantic_action_template_bootstrap_prompt`

- Stage: `pre_scene_action_parsing`
- Agent or module: `LLMSemanticActionTextPreprocessingModule`
- Role: induces the initial set of reusable action-text templates from the first episode, forming the basis for later action normalization.
- Main inputs: `instruction`, `episode_name`, and deduplicated `action_texts`.
- Main outputs: an `action_templates` list; each template is stored in `InducedTemplateRegistry`.
- Related artifacts: not written directly as a standalone output; it influences later `action_text_normalization.jsonl`, `action_templates.json`, and `action_name_map.json`.
- Note: this is the entry point of the semantic-template route used by the current default CLI path.
