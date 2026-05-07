# `passive_in_reveal_action_selection_prompt`

- Stage: `passive_observation_learning`
- Agent or module: `LLMContainableRevealActionSelectionModule`
- Role: selects which actions reveal the contents of containers and therefore can support learning passive `in(container, object)`-style observations.
- Main inputs: `action_summaries`, `predicate_comments`, and `containable_type_names`.
- Main outputs: `action_names` and `summary`.
- Related artifacts: not written directly on its own; the result influences which actions the passive-observation learner uses to build `in`-related evidence.
- Note: this is an action-level helper prompt.
