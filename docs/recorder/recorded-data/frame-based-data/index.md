# Frame-based data

The majority of Unity's components are intrinsically bound to the application update cycle: properties cannot be updated faster than the frame rate of the application. By default, the recorder will record the state of the environment at the end of each frame, with a maximum sampling rate defined in the `Update Rate` [setting](#settings).

The `FrameRecorderModule` is the orchestrator of the frame data recording process. It is responsible for asking each `FrameDataRecorderModule` for the data collected during the frame and automatically pack the data in a [Frame](../../file-format/proto-files/unity/frame.md#frame) sample.

## Settings

| Setting | Type | Description |
|---|---|---|
| Update Rate | int | Maximum number of frame per second that will be recorded by the `FrameRecorderModule`. The default value is 140Hz. Note that this is a soft limit and doesn't guarantee a perfect 140Hz sampling for example if your application slows down. |