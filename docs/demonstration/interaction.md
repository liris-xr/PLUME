# Analyze user interactions
Within the Easter Egg Hunt application, the user can teleport, pick up objects, grab eggs, etc. These low-level actions and interactions are defined within the Unity project.

## Record Input Actions
PLUME-Recorder records [Unity Input Actions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/Actions.html) which loosely correspond to input from the user (button pressed on the controller, position of the HMD, etc.).
For the Easter Egg Hunt project, actions are defined using the Input Action Manager component.

<p align="center">
    <img src="/demonstration/images/input_action_manager.png" alt="input action manager" width="800"/>
</p>

When an action is triggered, it sends a message to the PLUME-Recorder, which will timestamp and log the action. See more details on how PLUME-Recorder logs input actions [here](../recorder/recorded-data/inputs.md).

## Record interactions
PLUME-Recorder records XR Interaction Toolkit [interactable events](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/interactable-events.html) as well as [interactor events](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/interactor-events.html?q=interactor).
For each interactable and interactor present in the scene, PLUME-Recorder listens to these events. See more details on how PLUME-Recorder logs interactions in the [XRITK section](../recorder/recorded-data/inputs.md).

## Visually review interactions
Using PLUME-Viewer Interaction Heatmap module, you can highlight objects that have been interacted with. You can find the analysis module on the right side of the viewer.

* Interactor(s): copy and paste the GUID of one or more interactor. For example the right hand path is `XR Interaction Setup / XR Origin (XR Rig) / Camera Offset / Right Controller / Direct Interactor`.
* Interactable(s): copy and paste the GUID of one or more interactable. If empty, every interactable in the scene will be taken into account. For example the wine bottle path is `Livingroom / Props / Kitchen / Food / Wine Bottle`.
* Interaction type: For a Direct Interactor, `Hover` corresponds to touching an interactable, `Select` corresponds to grabbing an interactable, `Activate` is a contextual interaction executed with a selected interactable.
* Time Range: section of the record you want the heatmap to be computed on. Leave as is to take the entire record into account.

<p align="center">
    <img src="/demonstration/images/interaction_heatmap.png" alt="PLUME-Viewer interaction module" width="600"/>
</p>

Click on `Generate` to create the interaction heatmap with selected parameters. Once computed, objects that have been interacted with are highlighted in shades of red. White means no interaction, Dark Red means most number of interactions.

<p align="center">
    <img src="/demonstration/images/interaction_heatmap_result.png" alt="PLUME-Viewer interaction heatmap result" width="800"/>
</p>

Generated heatmaps can be hidden from view (using eye icon) or deleted (using trash icon).

## Compute interaction metrics
Using PLUME-Python, we can explore the recorded file to compute insighful metrics of our Easter egg hunt.

??? example "Count how many times objects have been hovered"
    Import required PLUME-Python classes and samples
    ```Python
    from plume_python.record import Record
    from plume_python.samples.unity.xritk.xr_base_interactable_pb2 import XRBaseInteractableHoverEnter
    ```

    Fetch data from XR Base Interactable Hover Enter samples and count the number of times the Interactable Hover Enter Event has been triggered for each interactable.
    ```Python
    def compute_hover_stats(record: Record) -> list[tuple[str, int]]:
    hovered_objects = {}
    for hover_sample in record.get_samples_by_type(XRBaseInteractableHoverEnter):
        object_id = hover_sample.payload.id.parent_id.game_object_id
        if object_id not in hovered_objects:
            hovered_objects[object_id] = 0
        hovered_objects[object_id] += 1
    return sorted(hovered_objects.items(), key=lambda x: x[1], reverse=True)
    ```

??? example "Count the number of teleportations"
    Import required PLUME-Python classes and samples
    ```Python
    from plume_python.record import Record
    from plume_python.samples.unity.xritk.xr_base_interactable_pb2 import XRBaseInteractableSelectEnter
    from plume_python.utils.game_object import find_first_name_by_guid
    ```

    In the Easter Egg Hunt scene, users teleport using a single [Teleportation Area](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.5/manual/teleportation-area.html). Counting how many times it has been selected corresponds to the effective number of teleportation.
    ```Python
    def compute_teleport_count(record: Record) -> int:
    count = 0
    for select_sample in record.get_samples_by_type(XRBaseInteractableSelectEnter):
        game_object_guid = select_sample.payload.id.parent_id.game_object_id
        game_object_name = find_first_name_by_guid(record, game_object_guid)
        if game_object_name == "Teleportation Area":
            count += 1
    return count
    ```

