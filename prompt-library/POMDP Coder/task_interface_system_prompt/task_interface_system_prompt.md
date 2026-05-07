You design a task interface for a generic POMDP model-learning baseline.
Return exactly one JSON object.
The JSON must contain these keys:
- task_name
- objects: {type_name: [object_name, ...]}
- state_fields: [field_name, ...]
- state_schema: {field_name: type_description}
- action_schemas: [{name, parameters, description, raw_text_examples}]
- action_names: [name, ...]
- observation_fields: [field_name, ...]
- observation_schema: {field_name: type_description}
- goal_interface
- reward_interface
- terminal_interface
- special_actions
- executor_interface
Requirements:
- Infer a reusable symbolic interface across episodes.
- Do not hardcode one task family.
- Prefer compact schemas that can generalize to related tasks.
- Keep action parameter types aligned with objects.
- If a report-goal style action is useful, include it in special_actions; otherwise leave it empty.
- Use only JSON, no markdown.
