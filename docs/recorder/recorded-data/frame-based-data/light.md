# Light

A light is a component that illuminates the scene (point light, directional light, spot light, etc.)

The `LightRecorderModule` automatically picks up every light in the scene and records:

- Whether the light is enabled or not
- Type (point, directional, spot, area)
- Shape
- Intensity
- Bounce Intensity
- Range
- Color
- Color Temperature
- Use Color Temperature
- Spot Angle
- Inner Spot Angle
- Shadows
- Shadow Strength
- Shadow Resolution
- Shadow Matrix Override
- Use Shadow Matrix Override
- Shadow Bias
- Shadow Normal Bias
- Shadow Near Plane
- Use View Frustum for Shadow Caster Cull
- Layer Shadow Cull Distances
- Shadow Custom Resolution
- Light Shadow Caster Mode
- Rendering Layer Mask
- Culling Mask
- Bounding Sphere Override
- Use Bounding Sphere Override
- Reference to the cookie texture asset
- Cookie Size
- Flare

## Creation and destruction

The creation and destruction of a light are recorded as a [LightCreate](../../advanced/format-specifications/unity/light.md#lightcreate) and [LightDestroy](../../advanced/format-specifications/unity/light.md#lightdestroy) sample respectively.

When created, a [LightUpdate](../../advanced/format-specifications/unity/light.md#lightupdate) sample is emitted with the initial properties of the light.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../contributing.md).

!!! info
    See the [associated proto files](../../advanced/format-specifications/unity/light.md) for more information on the data format.
