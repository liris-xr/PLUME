# Audio

The PLUME Recorder can be used to record the audio stream of the [AudioListener](https://docs.unity3d.com/Manual/class-AudioListener.html) component. When enabled, a `.wav` file containing the data stream from the `AudioListener` will be created alongside the main record file. Recorded audio is stereo and spatialized.

## Spatialized audio

The audio recorder module takes into account the audio setup of the project. As a consequence, the produced WAV file will have the same number of channels as the number of channels specified in the [audio speaker mode setting](https://docs.unity3d.com/ScriptReference/AudioSpeakerMode.html) (mono, stereo, quad, surroung, etc).
As the audio recorder module records the samples directly from the audio listener, it is also compatible with audio FX and spatializer plugins.

## Time synchronization

The audio system of Unity runs on a separated thread. As a result, the audio Digital Signal Processor (DSP) time might drift from the frame time. As a result, the audio recorder inserts silence in the WAV file when needed to re-synchronize the recorder's clock with the WAV time.

## Settings

| Setting | Type | Description |
|---|---|---|
| Enable | bool | Enable or disable the module. Disabled by default to prevent creating heavy WAV file when not required. |
| Log Silence Insertion | bool | When enabled, insertion of silence inside the `.wav` file will be logged in the Unity console. |