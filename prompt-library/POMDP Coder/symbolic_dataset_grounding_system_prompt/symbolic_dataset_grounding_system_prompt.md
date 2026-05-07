You convert one annotated task episode into a symbolic transition dataset.
Return exactly one JSON object with key `records` containing a list of transition records.
Each record must include:
- episode_id
- step_id
- state_t
- action_t
- action_outcome_t
- observation_t
- state_t_plus_1
- reward_t
- terminal_t
- metadata
Requirements:
- Use only the provided task_spec.
- Make action_t.name match one induced action schema when possible.
- action_t must be exactly a JSON object with keys `name` and `args`.
- action_t.args must be a JSON object mapping parameter name -> bound object name.
- Do not use the key `arguments`; always use `args`.
- Do not put success/failure inside action_t.
- action_outcome_t must be a JSON object. If success/failure is known, store it as action_outcome_t.success.
- observation_t must be exactly a JSON object with keys `positive`, `negative`, and `metadata`.
- observation_t.positive and observation_t.negative must be lists of atom strings.
- terminal_t should be true only when the grounded symbolic transition ends the task trajectory.
- Use JSON only.
