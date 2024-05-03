# Content size fitter

The `ContentSizeFitterRecorderModule` automatically picks up every [ContentSizeFitter](https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/script-ContentSizeFitter.html) component in the scene and records its properties.

## Creation and destruction

The creation and destruction of a ContentSizeFitter component are recorded as a [ContentSizeFitterCreate](../../../file-format/proto-files/unity/ui/content_size_fitter.md#contentsizefittercreate) and [ContentSizeFitterDestroy](../../../file-format/proto-files/unity/ui/content_size_fitter.md#contentsizefitterdestroy) sample respectively.

When created, a [ContentSizeFitterUpdate](../../../file-format/proto-files/unity/ui/content_size_fitter.md#contentsizefitterupdate) sample is emitted with the initial properties of the content size fitter component.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../contributing.md).

!!! info
    See the [associated proto files](../../../file-format/proto-files/unity/ui/content_size_fitter.md) for more information on the data format.