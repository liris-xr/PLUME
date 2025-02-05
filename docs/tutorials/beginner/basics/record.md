# Record an experiment

The PLUME Recorder is a Unity plugin that allows you to record data from any Unity application into a PLUME file (`.plm`). The plugin can be used on various type of projects (2D, 3D, XR) and platforms (Windows, Android, iOS).

## Installing the PLUME Recorder

!!! note
    PLUME Recorder requires Unity 2022 or later.

1. Go to `Window` > `Package Manager` > `Add package from git URL...`
2. Enter the Git URL and install: 
   ```{.copy}
   https://github.com/liris-xr/PLUME-Recorder.git
   ```
3. Force recompilation with hooks from `PLUME > Force Recompile With Hooks`

## Start/Stop a recording

By default, recording begins automatically when the application starts, so no additional action is needed. To manually control recording, disable the auto-start feature in the settings, then to start/stop the recordings, use:
``` { .csharp .copy }
PlumeRecorder.StartRecording()
```
and
``` { .csharp .copy }
PlumeRecorder.StopRecording()
```

## Record files

Records are stored in `.plm` files. This format is a binary file that contains all the data recorded during the experiment. It is decoupled from the Unity engine for external processing: you can extract and process data without the need for Unity.

After recording an experiment, the files can be found in the persistent data directory, located at:

* Windows: `C:/Users/<user>/AppData/LocalLow/<company name>`
* Android: `/storage/emulated/<userid>/Android/data/<packagename>/files`
* iOS: `/var/mobile/Containers/Data/Application/<guid>/Documents`
