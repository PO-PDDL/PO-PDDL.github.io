# `predicate_inventory_prompt`

- Stage: `manipulation_domain_learning`
- Agent or module: `LLMPredicateInventoryModule`
- Role: induces the global predicate inventory of the domain, including parameter types and predicate semantics.
- Main inputs: `instruction`, `taxonomy_records`, `action_texts` with observation and extra-info context, and optional `action_templates` and `available_types`.
- Main outputs: `predicate_inventory`, plus optional activation of special supertypes such as `movable_item`, `fixed_item`, and `containable_item`.
- Related artifacts: `predicate_inventory.json`, plus downstream effects on `action_schemas.pddl`, `manipulation_actions.pddl`, and effect validation.
- Note: the code enforces several required predicates, including `gripper_empty()` and `gripper_holding(movable_item)`.
