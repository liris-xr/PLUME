# Getting started

!!! info
    If you want to try PLUME on a sample project, you can use the [Easter Egg Hunt demo](https://www.github.com/liris-xr/PLUME-Demo).

To start using the PLUME toolbox, the first step is to install the recorder in your Unity project.

## 1. Installation 🛠️

### Prerequisites

* Unity 2022 or later

### Using the Unity Package Manager (Recommended)

1. Go to `Window` > `Package Manager` > `Add package from git URL...`
2. Enter the Git URL and install: `https://github.com/liris-xr/PLUME-Recorder.git`
3. Force recompilation with hooks from `PLUME > Force Recompile With Hooks`

!!! success
    The recorder is now installed and ready to record.

### Using Git

Clone the repository inside the `Packages` folder of your Unity project using the following command:

=== "HTTPS"
    
    ```bash
    git clone --recurse-submodules https://github.com/liris-xr/PLUME-Recorder.git
    ```

=== "SSH"

    ```bash
    git clone --recurse-submodules git@github.com:liris-xr/PLUME-Recorder.git
    ```


## 2. Record your experiment 🧪

By default, the record will start recording automatically as soon as the application starts so no specific action is required to start recording.
The recorder works both in the Unity Editor and in built applications on Windows/iOS/Android.

Records file will be saved in the [persistent data directory](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html) located at:

* Windows: `C:/Users/<user>/AppData/LocalLow/<company name>`
* Android: `/storage/emulated/<userid>/Android/data/<packagename>/files`
* iOS: `/var/mobile/Containers/Data/Application/<guid>/Documents`

If you want to start and stop the recording manually, you can disable the auto-start feature from the [settings](./global-settings.md) and use the `PlumeRecorder.StartRecording()` and `PlumeRecorder.StopRecording()` methods.

## 3. Quick inspection of the records 🔍

To ensure that nothing went wrong during the recording process, you can quickly inspect your record using the [PLUME Viewer](../viewer/index.md). See the dedicated page to [get started with the viewer](../viewer/getting-started.md).

## 4. In-situ and ex-situ analysis 🔬

After recording your experiment, you can analyze the data in-situ or ex-situ. See dedicated pages for getting started with [in-situ](../viewer/in-situ-analysis/index.md) analysis and [ex-situ](../python/ex-situ-analysis/index.md) analysis.