# Transform

Transforms are the objects' position, rotation and scale. The `TransformRecorderModule` picks up every transform in the scene and record:

- The local position: (x, y, z) position relative to its parent.
- The local rotation: (x, y, z, w) rotation quaternion relative to its parent.
- The local scale: (x, y, z) scale relative to its parent.
- The transform parent
- The transform sibling index

For efficient recording, new samples are emitted only when the difference in position, rotation or scale is significative enough to be considered as a change. Those threshold are defined in the [settings](#settings).

## Settings

| Setting | Type | Description |
|---|---|---|
| Position Threshold | float | Threshold over which movements will be effectively recorded. The value is expressed in local space. |
| Scale Threshold | float | Threshold over which the change in scale will be effectively recorded. The value is expressed in local space. |
| Scale Threshold | float | Threshold over which the change in scale will be effectively recorded. The value is expressed in local space. |