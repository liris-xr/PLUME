# Text

The `TMPTextRecorderModule` automatically picks up every [TextMeshProUGUI](https://docs.unity3d.com/Packages/com.unity.textmeshpro@4.0/api/TMPro.TextMeshProUGUI.html) component in the scene and records its properties.

## Creation and destruction

The creation and destruction of a Text component are recorded as a [TMPTextCreate](../../../../advanced/format-specifications/unity/ui/tmp_text.md#tmptextcreate) and [TMPTextDestroy](../../../../advanced/format-specifications/unity/ui/tmp_text.md#tmptextdestroy) sample respectively.

When created, a [TMPTextUpdate](../../../../advanced/format-specifications/unity/ui/tmp_text.md#tmptextupdate) sample is emitted with the initial text content and other properties of the Text component.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../../../contributing.md).

!!! info
    See the [associated proto files](../../../../advanced/format-specifications/unity/ui/tmp_text.md) for more information on the data format.