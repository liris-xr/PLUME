# Canvas renderer

The `CanvasRendererRecorderModule` automatically picks up every [CanvasRenderer](https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/class-CanvasRenderer.html) component in the scene and records its properties.

## Creation and destruction

The creation and destruction of a CanvasRenderer component are recorded as a [CanvasRendererCreate](../../../advanced/format-specifications/unity/ui/canvas_renderer.md#canvasrenderercreate) and [CanvasRendererDestroy](../../../advanced/format-specifications/unity/ui/canvas_renderer.md#canvasrendererdestroy) sample respectively.

When created, a [CanvasRendererUpdate](../../../advanced/format-specifications/unity/ui/canvas_renderer.md#canvasrendererupdate) sample is emitted with the initial properties of the CanvasRenderer component.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../../contributing.md).

!!! info
    See the [associated proto files](../../../advanced/format-specifications/unity/ui/canvas_renderer.md) for more information on the data format.