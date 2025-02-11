# Analyzing data ex-situ

Ex-situ analysis is the process of analyzing the data outside of the 3D context. For example to perform statistical analysis, machine learning, or to integrate the data in more traditional workflows. For this task, we provide PLUME Python, a Python package that allows you to load and extract data from PLUME record files. The package also comes with a set of utilities to simplify the conversion of the data into more commonly used formats in data analysis like pandas dataframe or CSV files. Embedded data such as LabStreamingLayer's samples can be exported to XDF files for external use in tools such as SigViewer, EEGLAB or MoBILAB.

## Installing PLUME Python

!!! note
    PLUME Python requires Python 3.10 or later.

In a Python environment (venv or conda), install the package using pip:

```bash
pip install plume-python
```

## Loading a record

!!! note
    A sample record file is available in the [tutorial repository](https://www.github.com/liris-xr/PLUME-Tutorial-Basics).

Reading a record file is done using the `RecordReader` class. The reader provides methods to access the data in the record file easily. A record file can contain multiple streams of data:

```
my_record_file.plm
├── frames
│   ├── frame_number: Number of the frame, as given by Unity Time.frameCount
│   ├── time_s: Time at which the frame was recorded in seconds, relative to the start of the recording.
│   ├── time_ns: Time at which the frame was recorded in nanoseconds, relative to the start of the recording.
|   ├── time_unix_s: Time at which the frame was recorded in seconds, relative to the UNIX epoch.
|   ├── ...
|   ├── scenes: All the scenes in the current frame.
|   |   ├── name: The name of the scene.
|   |   ├── guid: The globally unique identifier of the scene.
|   |   ├── ...
|   |   ├── game_objects: Game Objects in the scene, at this frame.
|   |   |   ├── name: The name of the Game Object.
|   |   |   ├── guid: The globally unique identifier of the Game Object.
|   |   |   ├── active: Whether the Game Object is active.
|   |   |   ├── tag: The tag of the Game Object.
|   |   |   ├── layer: The layer of the Game Object.
|   |   |   ├── ...
|   |   |   ├── components: Components attached the Game Object.
|   |   |   |   ├── guid: The globally unique identifier of the Component.
|   |   |   |   ├── ... (Component-specific data)
|   └── xritk_interactions: XR Interaction Toolkit interactions. This is frame-based because it relates interactions between XRInteractor and XRInteractable components in the scene.
├── markers: All the marker events in the record.
|   ├── label: The label of the marker.
|   ├── time_s: The time at which the marker was recorded in seconds, relative to the start of the recording.
|   ├── time_ns: The time at which the marker was recorded in nanoseconds, relative to the start of the recording.
|   
└── samples: All the samples in the record.
```

* **Frames**: Contains all the data that is frame-based (i.e. data that is updated in the Unity update loop). For example, the position of the objects, their properties, etc.
    * **Frame number**: The number of the frame, as given by Unity.
    * **Time**: The time at which the frame was recorded. Can be fetched as seconds or nano-seconds, relative to the start of the recording or in absolute UNIX time.
    * **Scenes**: All the scenes in the current frame.
        * **Scene name**: The name of the scene.
        * **Game Objects**: Game Objects in the scene.
            * **Components**: Components of the Game Object.

```python linenums="1"
from plume import RecordReader

reader = RecordReader("my_record_file.plm")

# Do something with the data

reader.close()
```

