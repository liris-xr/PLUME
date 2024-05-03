# Inputs

Inputs are the actions performed by the user in the application. This can be a button press, a trigger pull, a joystick movement, and so on.

The inputs are recorded by the `InputSystemRecorderModule` for the actions listed in the [XRITK input action manager](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/input-action-manager.html).

!!! info
    For now the `InputSystemRecorderModule` is still dependant on the XRITK input action manager. This will be updated in the future to decouple the input recording from the XRITK input action manager.

!!! info
    See the [associated proto file](../file-format/proto-files/unity/xritk/input_action.md) for more information on the data format.