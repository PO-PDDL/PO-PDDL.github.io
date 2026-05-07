# `object_typing_prompt`

- Stage: `manipulation_domain_learning`
- Agent or module: `LLMObjectTypingModule`
- Role: induces object types from action-argument usage and then uses them to type action schemas and related artifacts.
- Main inputs: `object_names` and `object_usage_examples`.
- Main outputs: an `object_types` list; the code then derives `object_type_map`, typed `taxonomy_records`, typed `action_templates`, and typed `action_schemas`.
- Related artifacts: `object_types.json`, `object_type_map.json`, and downstream updates to `action_schemas.json`, `action_templates.json`, and `action_name_map.json`.
- Note: this is the entry point for the type system used by later predicate and effect inference.
