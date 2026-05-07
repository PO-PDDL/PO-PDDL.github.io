# `visible_object_prompt`

Agent: `VisibleObjectExtractionAgent`

Used by:
- `generate_online_problem.py`

Role:
Extracts the visible scene objects that should become problem objects for online planning.

Trigger condition:
Used when `generate_online_problem.py` does not run with `--close-domain` and does not reuse an existing problem file.

Major inputs:
- domain_summary rendered from the parsed online-planning domain
- task instruction text
- image_input_note describing the scene image layout
- current scene image
- manipulation_records summary when available

Major outputs:
- JSON field `objects`
- each row contains `name`, `type_name`/`type`, and optional `justification`
- converted into `VisibleObject` and then `ObjectDeclaration` entries

Code path:
- `generate_online_problem.py` -> `POMDPDDL.online_planning_agent.cli` -> `OnlineProblemFileAgent` -> `VisibleObjectExtractionAgent.infer_visible_objects()`
