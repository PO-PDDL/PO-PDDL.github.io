# `predicate_comment_prompt`

- Stage: `manipulation_domain_learning`
- Agent or module: `LLMPredicateCommentModule`
- Role: generates human-readable comments for the learned predicates to improve rendered PDDL and manual inspection.
- Main inputs: `action_schemas` and `manipulation_records`.
- Main outputs: a `predicate_comments` dictionary keyed by predicate name.
- Related artifacts: `predicate_comments.json`, and downstream rendering of `action_schemas.pddl`, `manipulation_actions.pddl`, and later observation-learning context.
- Note: this prompt does not change semantics; it only documents them more clearly.
