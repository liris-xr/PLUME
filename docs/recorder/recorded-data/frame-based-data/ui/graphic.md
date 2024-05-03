# Graphic

The `GraphicRecorderModule` automatically picks up every Graphic component in the scene and records its properties.

## Creation and destruction

The Graphic component is an abstract type that is derived by UI elements such as Image, Text, etc. As a consequence, no creation sample is created by this recorder module, and update samples are emitted by the specific recorder modules for each derived type.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../contributing.md).

!!! info
    See the [associated proto files](../../../file-format/proto-files/unity/ui/graphic.md) for more information on the data format.