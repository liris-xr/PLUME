# Recording your first experiment

![PLUME Recorder](assets/recorder_teaser.png){ width="700" }
/// caption
///

The first brick of the PLUME toolbox is the PLUME Recorder. The PLUME Recorder is a Unity plugin that records the virtual environment, user behavior, and synchronized physiological signals into a single `.plm` file, without the need for extensive configuration and without having to modify the application's code. The plugin can be used on various type of projects (2D, 3D, XR), including multi-user experiences, and various platforms (Windows, Android, iOS), including standalone headsets.

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

By default, recording begins automatically when the application starts, so no additional action is needed. To manually control recording, disable the auto-start feature in the settings `PLUME > Settings > PLUME Recorder > Start On Play`, then to start/stop the recordings, use:
``` { .csharp .copy }
PlumeRecorder.StartRecording()
```
``` { .csharp .copy }
PlumeRecorder.StopRecording()
```

## Record files

Records are stored in `.plm` files. PLM files are self-contained binary files containing all the data recorded during the experiment. As it is self-contained, you can read it without the need for the original application or the Unity engine.

After recording an experiment, the files can be found in the persistent data directory, located at:

* Windows: `C:/Users/<user>/AppData/LocalLow/<company name>`
* Android: `/storage/emulated/<userid>/Android/data/<packagename>/files`
* iOS: `/var/mobile/Containers/Data/Application/<guid>/Documents`
