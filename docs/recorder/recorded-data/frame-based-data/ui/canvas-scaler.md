# Canvas scaler

The `CanvasScalerRecorderModule` automatically picks up every [CanvasScaler](https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/script-CanvasScaler.html) component in the scene and records its properties.

## Creation and destruction

The creation and destruction of a CanvasScaler component are recorded as a [CanvasScalerCreate](../../../advanced/format-specifications/unity/ui/canvas_scaler.md#canvasscalercreate) and [CanvasScalerDestroy](../../../advanced/format-specifications/unity/ui/canvas_scaler.md#canvasscalerdestroy) sample respectively.

When created, a [CanvasScalerUpdate](../../../advanced/format-specifications/unity/ui/canvas_scaler.md#canvasscalerupdate) sample is emitted with the initial properties of the CanvasScaler component.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../../contributing.md).

!!! info
    See the [associated proto files](../../../advanced/format-specifications/unity/ui/canvas_scaler.md) for more information on the data format.