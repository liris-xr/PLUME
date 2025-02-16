# Analyzing data ex-situ

Ex-situ analysis is the process of analyzing the data outside of the 3D context. For example to perform statistical
analysis, machine learning, or to integrate the data in more traditional workflows. For this task, we provide PLUME
Python, a Python package that allows you to load and extract data from PLUME record files. The package also comes with a
set of utilities to simplify the conversion of the data into more commonly used formats in data analysis like pandas
dataframe or CSV files. Embedded data such as LabStreamingLayer's samples can be exported to XDF files for external use
in tools such as SigViewer, EEGLAB or MoBILAB.

## Installing PLUME Python

!!! note
PLUME Python requires Python 3.10 or later.

In a Python environment (venv or conda), install the package using pip:

```bash
pip install plume-python
```

## Parsing a record

!!! note
A sample record file is available in the [tutorial repository](https://www.github.com/liris-xr/PLUME-Tutorial-Basics).

Record files can be accessed through the `RecordReader` class, which offers convenient methods for navigating the data. Within each record file, you'll find four primary data streams:

1. **Frames**: Contains frame-by-frame data including:
    - Basic timing information (frame number, timestamps)
    - Scene hierarchy with GameObjects and their Components
    - XR Interaction Toolkit interactions

2. **Markers**: Event markers with labels and timestamps, used for annotating specific moments in your recording

3. **Signals**: Time-series data (like LSL physiological signals) with:
    - Stream information (name, type, channel count)
    - Sample values with precise timestamps

4. **Input Actions**: Records of user inputs (keyboard, mouse, etc.) with:
    - Binding paths
    - Action types
    - Precise timestamps

```python linenums="1"
from plume import RecordReader

reader = RecordReader("my_record_file.plm")

# Do something with the data

reader.close()
```

### Example: Extracting the position of a GameObject

```python exec="on" source="above" linenums="1" session="record-parsing"
from plume import RecordReader
import numpy as np
import plotly.graph_objects as go
import matplotlib
from tqdm import tqdm

reader = RecordReader("docs/tutorials/beginner/basics/assets/record.plm")

time_s = np.empty(0)
world_positions: np.ndarray = np.empty((0, 3))

for frame in tqdm(reader.frames):
    scene = frame.scenes.first_with_name("HouseObjectivesSteamAudio")
    player = scene.game_objects.first_with_name("Torso")
    world_pos = player.transform.world_position.numpy()
    world_positions = np.append(world_positions, world_pos.reshape(1, 3), axis=0)
    time_s = np.append(time_s, frame.time_s)

markers = [marker for marker in reader.markers]
marker_time_s = np.array([marker.time_s for marker in markers])
marker_labels = [marker.label for marker in markers]
# for each marker, find its closest world position
marker_positions: np.ndarray = np.empty((0, 3))
for marker in markers:
    marker_pos = world_positions[np.argmin(np.abs(time_s - marker.time_s))]
    marker_positions = np.append(marker_positions, marker_pos.reshape(1, 3), axis=0)

max_time = max(time_s)
min_time = min(time_s)
colors = matplotlib.colormaps["viridis"]((time_s - min_time) / (max_time - min_time))

fig = go.Figure(
    data=go.Scatter3d(
        name="Path",
        x=world_positions[:, 0],
        y=world_positions[:, 2],
        z=world_positions[:, 1],
        line=dict(color=colors, width=5),
        mode="lines",
    )
)

fig.add_trace(
    go.Scatter3d(
        x=world_positions[[0, -1], 0],
        y=world_positions[[0, -1], 2],
        z=world_positions[[0, -1], 1],
        mode="markers+text",
        name="Start/End",
        text=["Start", "End"],
        textposition="top center",
    )
)

fig.add_trace(
    go.Scatter3d(
        x=marker_positions[:, 0],
        y=marker_positions[:, 2],
        z=marker_positions[:, 1],
        mode="markers+text",
        name="Markers",
        text=marker_labels,
        textposition="top center",
    )
)

fig.update_layout(
    autosize=True,
    scene=dict(
        camera=dict(
            up=dict(x=0, y=0, z=1),
            eye=dict(
                x=0,
                y=1.0707,
                z=1,
            ),
        ),
        aspectratio=dict(x=1, y=1, z=1),
        aspectmode="manual",
    ),
)

fig.show()
reader.close()
```

```python exec="true" html="true" session="record-parsing"
import plotly.express as px
print(fig.to_html(full_html=False, include_plotlyjs="cdn"))
```
