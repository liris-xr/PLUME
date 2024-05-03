# Image

The `ImageRecorderModule` automatically picks up every [Image](https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/script-Image.html) component in the scene and records its properties.

## Creation and destruction

The creation and destruction of an Image component are recorded as an [ImageCreate](../../../file-format/proto-files/unity/ui/image.md#imagecreate) and [ImageDestroy](../../../file-format/proto-files/unity/ui/image.md#imagedestroy) sample respectively.

When created, an [ImageUpdate](../../../file-format/proto-files/unity/ui/image.md#imageupdate) sample is emitted with the initial sprite and other properties of the Image component.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../contributing.md).

!!! info
    See the [associated proto files](../../../file-format/proto-files/unity/ui/image.md) for more information on the data format.