# Canvas

The `CanvasRecorderModule` automatically picks up every [Canvas](https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/UICanvas.html) component in the scene and records its properties.

## Creation and destruction

The creation and destruction of a Canvas component are recorded as a [CanvasCreate](../../../file-format/proto-files/unity/ui/canvas.md#canvascreate) and [CanvasDestroy](../../../file-format/proto-files/unity/ui/canvas.md#canvasdestroy) sample respectively.

When created, a [CanvasUpdate](../../../file-format/proto-files/unity/ui/canvas.md#canvasupdate) sample is emitted with the initial properties of the Canvas component.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../contributing.md).

!!! info
    See the [associated proto files](../../../file-format/proto-files/unity/ui/canvas.md) for more information on the data format.