# Get started

PLUME is a toolbox composed of three main tools:

- [PLUME Recorder](./recorder/index.md) for recording data from any Unity applications.
- [PLUME Viewer](./viewer/index.md) for replaying records and in-situ analysis.
- [PLUME Python](./python/index.md) for ex-situ analysis.

The following guide will help you get started with PLUME by recording your first experiment, reviewing it in the viewer and analyzing the data.

## 1. Recording your experiment and collect data 🧪

1. Install the PLUME Recorder in your Unity project by following the [installation guide](./recorder/installation.md) (2min setup).
2. Build your application for deployment on Windows/iOS/Android or run it in the Unity Editor.
3. By default, the record will start recording automatically as soon as the application starts so no specific action is required to start recording. Records file will be saved as `.plm` files in the [persistent data directory](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html) located at:
      * Windows: `C:/Users/<user>/AppData/LocalLow/<company name>`
      * Android: `/storage/emulated/<userid>/Android/data/<packagename>/files`
      * iOS: `/var/mobile/Containers/Data/Application/<guid>/Documents`

## 1.1. Recording event markers

The recorder provides a way to easily record event markers. For this, you can place the following code snippet in any of your Unity scripts:

```csharp
PlumeRecorder.RecordMarker("MyMarkerLabel");
```

## 1.2. Recording physiological data

By default, the recorder automatically will record any physiological data stream from the [LabStreamingLayer](https://labstreaminglayer.org/#/) (LSL) and synchronize it with the timestamp system of PLUME.

To record data from your own physiological hardware, start by checking the [list of supported devices](https://labstreaminglayer.readthedocs.io/info/supported_devices.html) to see if a script to stream data to LSL already exists for your device. If not, you can easily create a script to stream data to LSL by using libraries implementing the LSL protocol such as [pylsl](https://pypi.org/project/pylsl/), see an example [here](https://github.com/labstreaminglayer/pylsl/blob/cbddf03f3e6b644762b016d66d9347b4a3169865/pylsl/examples/SendData.py).

## 1.3. Recording custom data

Please refer to the [recording custom data guide](./recorder/advanced/recording-custom-data.md).

## 2. Quick inspection of the records 🔍

To ensure that nothing went wrong during the recording process, you can quickly inspect `.plm` files by replaying them in the [PLUME Viewer](./viewer/index.md).

<video width="800" height="600" controls autoplay loop>
    <source src="../viewer/videos/replay.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

1. Install the PLUME Viewer by following the [installation guide](./viewer/installation.md).
2. In your Unity project, export the asset bundle (only required once) by following the [export guide](./recorder/advanced/asset-bundle.md#exporting-an-asset-bundle). This asset bundle contains the assets required to visualize the record.
3. Open the PLUME Viewer and load the record file (`.plm` file) and asset bundle by following the [replay guide](./viewer/replay.md). 

## 3. In-situ analysis (using the viewer) 🔬

After quickly inspecting your record, you can now perform [in-situ analysis](./viewer/in-situ-analysis/index.md) using the viewer. The viewer provides a set of modules to visualize and analyze the data within the 3D context such as [3D trajectories](./viewer/in-situ-analysis/trajectories.md), [position heatmap](./viewer/in-situ-analysis/position-heatmap.md), [eye-gaze heatmap](./viewer/in-situ-analysis/eye-gaze-heatmap.md) and [interactions highlights](./viewer/in-situ-analysis/interactions-highlights.md).

## 4. Ex-situ analysis (using Python) 🔬

PLUME record files are fully decoupled from any application. As a result, they can be parsed from any applications using the Protobuf library. To further simplify the process, we provide a Python API to easily parse and extract data from the record files. This allows you to perform [ex-situ analysis](./python/ex-situ-analysis/index.md) using Python for more traditional analysis workflow (statistical analysis, machine learning, etc.).

1. Install the Python package using pip:
    ```bash
    pip install plume-python
    ```
2. You can now parse a record file and extract data using the Python API. 
    ```python
    import plume_python as plm

    # Load a record file
    record = plm.parser.parse_record_from_file("path/to/record.plm")
    ```
3. You can now extract data from the record file and perform any analysis you want. See the [usage guide](./python/usage.md) for more information.
