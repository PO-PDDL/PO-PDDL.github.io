# Init Program Proposal

Write a Python function `sample_initial_state(rng)` for the task-specific API.
Do not rely on any benchmark or task name; use only the provided interface, schema, and examples.

Your job is to model the hidden world state at the start of an episode, before any new action is executed.

Important modeling rules:

- Learn from initial-state evidence, not from future-goal text.
- Treat the instruction and `goal_spec` as desired future outcomes, not as permission to place objects directly at their goal locations at time 0.
- Use the representative examples as initial-state supervision. If an object repeatedly appears with a concrete initial location, preserve that object-specific prior instead of collapsing everything into a generic pooled movable-object distribution.
- Do not over-generalize `unknown`. Use `unknown` only when the examples suggest the object's initial location is genuinely hidden or unspecified.
- If an object is frequently concrete in earliest states but becomes `unknown` in unrelated examples, do not let those unrelated placeholder states dominate its initial prior.
- Prefer coherent per-object priors. Different movable objects may have different initial-location patterns.
- When examples show an object initially on top of a drawer, in front of a drawer, or inside a drawer, model those location families explicitly.
- Avoid initializing the target object as already satisfying the goal unless the examples genuinely support that as a common initial condition.
- Keep the model simple and stochastic, but make the randomness reflect the example distribution rather than a uniform fallback over all movable objects.

What good solutions usually do:

- infer a small number of object-specific initial-location modes from the earliest episode states;
- keep drawer/open-state uncertainty separate from object-location uncertainty;
- use `unknown` mainly for hidden-in-drawer or genuinely unseen objects;
- allow distractor objects to stay sparse while keeping task-relevant objects well modeled.
