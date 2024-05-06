# Installation

!!! info
    If you want to try PLUME on a sample project, you can use the [Easter Egg Hunt demo](https://www.github.com/liris-xr/PLUME-Demo).

To start using the PLUME toolbox, the first step is to install the recorder in your Unity project.

## Prerequisites

* Unity 2022 or later

## Using the Unity Package Manager 📦 **(Recommended)**

1. Go to `Window` > `Package Manager` > `Add package from git URL...`
2. Enter the Git URL and install: `https://github.com/liris-xr/PLUME-Recorder.git`
3. Force recompilation with hooks from `PLUME > Force Recompile With Hooks`

!!! success
    The recorder is now installed and ready to record.

By default, the record will start recording automatically as soon as the application starts so no specific action is required to start recording. Records file will be saved in the [persistent data directory](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html) located at:

   * Windows: `C:/Users/<user>/AppData/LocalLow/<company name>`
   * Android: `/storage/emulated/<userid>/Android/data/<packagename>/files`
   * iOS: `/var/mobile/Containers/Data/Application/<guid>/Documents`

If you want to start and stop the recording manually, you can disable the auto-start feature from the [settings](./global-settings.md) and use the `PlumeRecorder.StartRecording()` and `PlumeRecorder.StopRecording()` methods.

## Using Git 🐙

Clone the repository inside the `Packages` folder of your Unity project using the following command:

=== "HTTPS"
    
    ```bash
    git clone --recurse-submodules https://github.com/liris-xr/PLUME-Recorder.git
    ```

=== "SSH"

    ```bash
    git clone --recurse-submodules git@github.com:liris-xr/PLUME-Recorder.git
    ```
