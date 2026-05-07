# `runtime_observation_prompt`

Stage: runtime multimodal observation grounding

Role:
Asks a multimodal LLM to judge which candidate observable atoms are visually supported at the current step.

Trigger condition:
Used when the interactive runtime decides that the current belief and action have informative candidate observable atoms and therefore issues an observation-grounding request.

Major inputs:
- task_name
- instruction
- current action
- known_objects
- state_fields
- observation_fields
- candidate_observable_atoms
- image_input_note
- executor-returned image content

Major outputs:
- one JSON object with `observable_judgments`, `new_objects`, and `notes`
- converted into the runtime observation payload with `positive`, `negative`, and `metadata`

Runtime assembly note:
This prompt is built by `pomdp_coder.runtime.observation_interface.build_observation_prompt(...)`. The body is fixed, but the final context JSON is parameterized by the current runtime state, current action, and candidate observable atoms.
