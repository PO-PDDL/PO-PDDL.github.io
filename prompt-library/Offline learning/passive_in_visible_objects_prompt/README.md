# `passive_in_visible_objects_prompt`

- Stage: `passive_observation_learning`
- Agent or module: `LLMVisibleContainedObjectsModule`
- Role: decides which candidate objects are visually seen inside a given container in the current record.
- Main inputs: `record`, `container_object_name`, `candidate_object_names`, and `predicate_comments`.
- Main outputs: `visible_object_names` and `summary`.
- Related artifacts: not written directly as a separate file; the result contributes to passive-observation evidence and helps learn `in`-style rules.
- Note: this prompt provides object-level evidence about visible container contents.
