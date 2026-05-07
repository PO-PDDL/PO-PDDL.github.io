# `semantic_action_template_resolution_prompt`

- Stage: `pre_scene_action_parsing`
- Agent or module: `LLMSemanticActionTextPreprocessingModule`
- Role: resolves an action text that does not match any existing template by deciding whether it should map to an existing template or create a new one.
- Main inputs: `instruction`, `existing_action_templates`, and one `unmatched_action`.
- Main outputs: `resolution_kind`, `placeholder_values`, and either `matched_template_id` or `new_action_template`.
- Related artifacts: not written directly as a standalone output; the result appears in normalized action text records and the evolving template set.
- Note: this is a prompt-level template repair mechanism for preprocessing, not a domain-repair stage.
