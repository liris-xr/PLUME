# Audio

The audio stream from the [AudioListener](https://docs.unity3d.com/Manual/class-AudioListener.html) is automatically recorded when the `AudioRecorderModule` is enabled in the settings. The audio is recorded as a `.wav` file alongside the record file.

!!! warning
    The audio recorder module is disabled by default in the settings. If you want to record audio, make sure to enable it before running your experiment.

## Spatialized audio

The audio recorder module takes into account the audio setup of the project. As a consequence, the produced WAV file will have the same number of channels as the number of channels specified in the [audio speaker mode setting](https://docs.unity3d.com/ScriptReference/AudioSpeakerMode.html) (mono, stereo, quad, surroung, etc).
As the audio recorder module records the samples directly from the audio listener, it is also compatible with audio FX and spatializer plugins.

## Time synchronization

The audio system of Unity runs on a separated thread. As a result, the audio Digital Signal Processor (DSP) time might drift from the frame time. As a result, the audio recorder inserts silence in the WAV file when needed to re-synchronize the recorder's clock with the WAV time.

## Settings

| Setting               | Type | Description                                                                                             |
| --------------------- | ---- | ------------------------------------------------------------------------------------------------------- |
| Enable                | bool | Enable or disable the module. Disabled by default to prevent creating heavy WAV file when not required. |
| Log Silence Insertion | bool | When enabled, insertion of silence inside the `.wav` file will be logged in the Unity console.          |