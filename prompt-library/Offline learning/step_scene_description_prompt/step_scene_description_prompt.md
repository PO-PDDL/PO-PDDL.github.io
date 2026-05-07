You are given:
- the task instruction,
- all prior steps, including their action text, failure marker if any, and previously generated scene descriptions,
- the current step's action text and failure marker if any,
- the ordered image sequence for the current step,
- the ordered future action sequence,
- `allowed_object_names`, the complete list of objects you are allowed to mention for this episode,
- and `current_step_focus_objects`, the current step's main target objects.

Write the current step's scene description in English.

Hard constraints:
- `allowed_object_names` is a hard constraint on which objects may be mentioned.
- Only describe objects that are both visually supported and present in `allowed_object_names`.
- If an object is visible but not in `allowed_object_names`, do not describe it.
- All task-relevant objects use unique names in the instruction and action texts.
- The same object name always refers to the same real object across all steps and all camera views.
- If the same named object appears from multiple camera views or viewpoints during this step, it is still the same object, not multiple objects.
- Never split one named object into multiple objects just because it appears in different views or at different moments in the sequence.
- If the scene seems to contain two visually similar task-relevant objects, carefully decide which one is more likely to be the true task-relevant object named in the task context, and describe only that one.
- Do not hedge by describing multiple similar objects under the same task-relevant name.
- Do not describe one object as being in multiple incompatible locations or relations at the same time.

Core rules:
- The image sequence is the primary evidence for the current step.
- The last frame is the main target for description because it best represents the world state after the action is completed.
- Earlier frames are reference evidence only. Use them to resolve ambiguity, identify objects, or understand what changed, but do not let them override the final visible world state in the last frame.
- Prior scene descriptions provide memory about previously observed objects and states.
- The current action text, the ordered future action sequence, and the instruction are only focus and naming hints.
- `current_step_focus_objects` tells you which allowed objects deserve the most attention for this step.
- They help you decide what to pay attention to and how to name things.
- They are not evidence for hidden objects, hidden states, or unobserved outcomes.
- Use the future action sequence exactly like in the init-step scene description: only to help decide which objects deserve attention and how to name them consistently.
- If the same object name appears multiple times in the task context, it refers to the same real object in the scene.

Requirements:
1. Describe the final visible result of the current step.
   - Describe the final static scene, not the motion itself.
   - Mainly describe the last frame, because it represents the action-completed world state.
   - Use earlier frames only as supporting reference when the last frame is ambiguous, partially occluded, or less clear.
2. Only describe explicitly named task objects.
   - A visible object may be described only if it appears in `allowed_object_names`.
   - If an object is visible but absent from `allowed_object_names`, leave it out of the scene description.
   - Do not duplicate one named object into multiple described objects across views or across frames.
   - If multiple similar candidates are visible, choose the single candidate most likely to match the named task object and describe only that one.
3. If the step mainly reveals information rather than changing world state, summarize what becomes observable.
   - If something is clearly seen in the middle of the sequence and remains true, include it even if the last frame is less clear.
   - Keep the description centered on the target of the current step.
4. Focus on what changed or what was newly revealed.
   - Prefer the state change caused by the action, or the newly observed objects and states revealed by the action.
   - Do not repeat unrelated old facts.
   - Only bring in prior facts when they are needed to understand the current target.
5. Maintain memory across steps.
   - If an object was previously observed somewhere and no later action removed it, keep that in mind.
   - Do not drop such facts just because the current viewpoint is imperfect.
   - Use memory to support accurate target-focused descriptions, not to re-summarize the whole scene.
6. Use task context only to guide focus and naming.
   - Reuse object names and state phrases from the instruction, current action text, prior action texts, future action sequence, and prior scene descriptions when they fit the visual evidence.
   - Prefer stable task vocabulary over paraphrases.
   - If later actions distinguish visible objects by color, type, or role, preserve that distinction when visually supported.
   - Treat repeated uses of the same object name as references to the same object across steps.
   - Treat the same named object seen from different camera views or different frames as the same single object.
   - Do not introduce a visible object into the description unless it is in `allowed_object_names`.
   - If a later action explicitly opens a named object such as a drawer, box, cabinet, lid, or door, then when the current image sequence is ambiguous you should prefer interpreting that object as currently closed rather than already open.
   - Use this only as a tie-breaker under visual ambiguity; if the images clearly show the object already open, describe it as open.
7. Stay visually grounded and conservative.
   - Do not invent hidden objects or hidden state changes.
   - Do not use future actions as evidence that something is currently visible or changed.
   - Omit doubtful claims rather than hallucinating them.
8. If the current step is marked as failed, use the image sequence and failure marker to describe the actual visible outcome rather than the intended outcome.
   - Pay extra attention to the state of the action-relevant objects in failed steps.
   - Especially describe their resulting physical state, location, support relation, containment relation, or relative position to other task objects when these are visually clear.
   - Do not replace physical state/location with image-layout wording such as "near the front edge of the scene", "in the top-left of the image", or other camera-frame positions.
   - Prefer world-state descriptions such as "on top of the drawer", "inside the drawer", "next to the drawer", "still in the gripper", or "on the table near the drawer" when visually supported.
9. If a human hand or robot gripper is clearly visible and relevant, describe whether it is empty or holding something.
10. Keep the scene description concise but complete.
   - One or two short sentences are usually enough.
11. Naming discipline matters.
   - Prefer exact wording already present in the task context when the images support it.
   - Avoid unnecessary renaming or introducing alternate labels for the same object or state.
   - If a visible object is not in `allowed_object_names`, leave it out instead of inventing a label for it.
   - Do not assign one object multiple incompatible locations or relations in the same description.
12. Prefer physical world descriptions over camera-layout descriptions.
   - Describe where an object is in the scene relative to task objects or supports, not where it appears in the image.
   - Avoid phrases based only on image coordinates, screen regions, or view-centered directions unless they are explicitly part of the task/world vocabulary.

Return JSON only:
{
  "scene_description_text": "..."
}
