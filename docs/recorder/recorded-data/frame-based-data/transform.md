# Transform

Transforms contain the objects' position, rotation and scale.

The `TransformRecorderModule` automatically picks up every transform in the scene and records:

- Local position: (x, y, z) position relative to its parent.

    !!! note
        The position is expressed in local space, this means that depending on the scale of its parents in the hierarchy, the value might not be expressed in meters. If you need to work with world positions, see how to [convert local positions to world positions](#convert-local-positions-to-world-positions).

- Local rotation: (x, y, z, w) rotation quaternion relative to its parent.
- Local scale: (x, y, z) scale relative to its parent.
- Sibling index
- Reference to the transform's parent

For efficient recording, new samples are emitted only when the difference in position, rotation or scale is significative enough to be considered as a change. Those threshold are defined in the [settings](#settings).

## Creation and destruction

The creation and destruction of a transform are recorded as a [TransformCreate](../../advanced/format-specifications/unity/transform.md#transformcreate) and [TransformDestroy](../../advanced/format-specifications/unity/transform.md#transformdestroy) sample respectively.

When created, a [TransformUpdate](../../advanced/format-specifications/unity/transform.md#transformupdate) sample is emitted with the initial position, rotation, scale, parent and sibling index.

## Update

### Polling

As transforms can be updated internally by the physics engine, and as we cannot inject hooks in the Unity Engine (mainly for legal reasons), we are constrained to poll changes in the transform's position, rotation and scale at the end of the frame. In order to keep high performance, we use the Burst compiler to detect the changes in parallel with optimized code. Every time a change is detected and is above the defined threshold in the [settings](#settings), a [TransformUpdate](../../advanced/format-specifications/unity/transform.md#transformupdate) sample is emitted with the updated position, rotation and scale.

### Hooks

A [TransformUpdate](../../advanced/format-specifications/unity/transform.md#transformupdate) sample is emitted when a change in the hierarchy is detected. The following methods are hooked to detect those changes:

- [void Transform.SetParent(Transform p)](https://docs.unity3d.com/ScriptReference/Transform.SetParent.html)
- [void Transform.SetParent(Transform p, bool worldPositionStays)](https://docs.unity3d.com/ScriptReference/Transform.SetParent.html)
- [Transform.parent](https://docs.unity3d.com/ScriptReference/Transform-parent.html)
- [void Transform.SetSiblingIndex(int index)](https://docs.unity3d.com/ScriptReference/Transform.SetSiblingIndex.html)
- [void Transform.SetAsFirstSibling()](https://docs.unity3d.com/ScriptReference/Transform.SetAsFirstSibling.html)
- [void Transform.SetAsLastSibling()](https://docs.unity3d.com/ScriptReference/Transform.SetAsLastSibling.html)

## Settings

Settings for the `TransformRecorderModule` can be found under `Edit > Project Settings > PLUME Recorder > Frame Recorder > Transform`.

| Setting            | Type  | Description                                                                                                   |
| ------------------ | ----- | ------------------------------------------------------------------------------------------------------------- |
| Position Threshold | float | Threshold over which movements will be effectively recorded. The value is expressed in local space.           |
| Scale Threshold    | float | Threshold over which the change in scale will be effectively recorded. The value is expressed in local space. |
| Scale Threshold    | float | Threshold over which the change in scale will be effectively recorded. The value is expressed in local space. |

!!! info
    See the [associated proto files](../../advanced/format-specifications/unity/transform.md) for more information on the data format.