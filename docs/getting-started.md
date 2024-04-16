# Getting Started

## Install the recorder 📦

Before installing the recorder, ensure that your project is using Unity 2022 or later.

1. Go to `Window` > `Package Manager` > `Add package from git URL...`
2. Enter the Git URL and install: `https://github.com/liris-xr/PLUME-Recorder.git`
3. Force recompilation with hooks from `PLUME > Force Recompile With Hooks`

!!! success
    The recorder is now installed and ready to record.

## Record your experiment 🧪

By default, the record will start recording automatically as soon as the application starts so no specific action is required to start recording.
The recorder works both in the Unity Editor and in built applications on Windows/iOS/Android.

Records file will be saved in the [persistent data directory](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html) located at:

* Windows: `C:/Users/<user>/AppData/LocalLow/<company name>`
* Android: `/storage/emulated/<userid>/Android/data/<packagename>/files`
* iOS: `/var/mobile/Containers/Data/Application/<guid>/Documents`

## Quick inspection of the records 🔍

To ensure that nothing went wrong during the recording process, you can quickly inspect your record using the [PLUME Viewer](./viewer/index.md).

1. Build the asset bundle by going to `PLUME > Build Asset Bundle`. An archive named `plume_bundle.zip` will be generated under `Assets/AssetBundles/`.

    !!! info
        This step is only required once as it is common to every records for a given project.

2. Download the latest version of the PLUME Viewer from the [GitHub releases page](https://github.com/liris-xr/PLUME-Viewer/releases).
3. Execute `PLUME-Viewer.exe` and select your record file (`.plm`) then select the asset bundle (`plume_bundle.zip`).

    !!! tip
        You can associate the `.plm` file extension to `PLUME-Viewer.exe` to quickly open record files in the viewer.
    !!! tip
        By default, the viewer will look for the asset bundle next to the record file. By placing the `plume_bundle.zip` in the same folder as the `.plm` files, the viewer will not ask for it when opening a record.

## In-situ and ex-situ analysis 🔬

See dedicated pages for getting started with [in-situ analysis](./viewer/in-situ-analysis/index.md) and [ex-situ analysis](./python/ex-situ-analysis/index.md).
