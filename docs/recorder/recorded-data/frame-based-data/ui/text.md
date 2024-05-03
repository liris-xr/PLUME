# Text

The `TextRecorderModule` automatically picks up every [Text](https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/script-Text.html) component in the scene and records its properties.

## Creation and destruction

The creation and destruction of a Text component are recorded as a [TextCreate](../../../file-format/proto-files/unity/ui/text.md#textcreate) and [TextDestroy](../../../file-format/proto-files/unity/ui/text.md#textdestroy) sample respectively.

When created, a [TextUpdate](../../../file-format/proto-files/unity/ui/text.md#textupdate) sample is emitted with the initial text content and other properties of the Text component.

## Update

### Hooks

A [TextUpdate](../../../file-format/proto-files/unity/ui/text.md#textupdate) sample is emitted when a change in the component properties is detected. The following methods are hooked to detect those changes:

- [Text.text](https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/script-Text.html)

!!! info
    See the [associated proto files](../../../file-format/proto-files/unity/ui/text.md) for more information on the data format.