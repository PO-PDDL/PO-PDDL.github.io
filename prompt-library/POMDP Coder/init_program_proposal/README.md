# `init_program_proposal`

Stage: `4_initial_program_proposal`

Role:
Learns the initial-state sampler.

Trigger condition:
Used in Stage 4 to generate initial candidate programs for the `init` component.

Major inputs:
- base proposal prompt text
- execution_rules.md
- init_program_spec.md
- shared_api_context.json
- representative_train_examples
- starter template file

Major outputs:
- a complete Python candidate program
- must define `sample_initial_state`
- stored as candidate code plus prompt/response artifacts

Runtime assembly note:
The pipeline does not send this file alone. It prepends/appends execution rules, component spec, shared API context, representative train examples, and the starter template to build the final system prompt.
