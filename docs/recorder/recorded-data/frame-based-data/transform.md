# Transform

Transforms are the objects' position, rotation and scale. The `TransformRecorderModule` picks up every transform in the scene and record:

- The local position: (x, y, z) position relative to its parent.
- The local rotation: (x, y, z, w) rotation quaternion relative to its parent.
- The local scale: (x, y, z) scale relative to its parent.
- The transform parent
- The transform sibling index

For efficient recording, new samples are emitted only when the difference in position, rotation or scale is significative enough to be considered as a change. Those threshold are defined in the [settings](#settings).

## Hooks

Due to the nature of the transform, any change in position, rotation and scale is not handled by hooks but via Burst compiled jobs that are executed at the end of the frame. Only functions related to changes in the hierarchy gets intercepted by hooks:

- [SetParent](https://docs.unity3d.com/ScriptReference/Transform.SetParent.html)
- [SetSiblingIndex](https://docs.unity3d.com/ScriptReference/Transform.SetSiblingIndex.html)

## Settings

| Setting | Type | Description |
|---|---|---|
| Position Threshold | float | Threshold over which movements will be effectively recorded. The value is expressed in local space. |
| Scale Threshold | float | Threshold over which the change in scale will be effectively recorded. The value is expressed in local space. |
| Scale Threshold | float | Threshold over which the change in scale will be effectively recorded. The value is expressed in local space. |