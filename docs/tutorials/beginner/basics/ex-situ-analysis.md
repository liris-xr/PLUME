# Analyzing data ex-situ

Ex-situ analysis is the process of analyzing the data outside its 3D context. For example to perform statistical
analysis, machine learning and to integrate the data in more traditional workflows. For this task, we provide PLUME
Python, a Python package that allows you to load and extract data from PLUME record files. The package also comes with a
set of utilities to simplify the conversion of the data to different formats used in data analysis like pandas
dataframe, CSV and XDF for physiological signals to be analyzed in external software such as SigViewer, EEGLAB or
MoBILAB.

## Installing PLUME Python

!!! note
    PLUME Python requires Python 3.10 or later.

In a Python environment (venv or conda), install the package using pip:

```bash
pip install plume-python
```

## Reading data from a record file

!!! note
    A sample record file is available in the [tutorial repository](https://www.github.com/liris-xr/PLUME-Tutorial-Basics).

Record files data can be accessed through the `RecordReader` class, which offers convenient methods for navigating the
data. To start with a basic example, let's extract and plot the position of a GameObject over time, in our case, we will take the position of the player's `Head` and plot its 3D trajectory. First, we need to import the necessary libraries and create a `RecordReader` object:

```python linenums="1"
from plume import RecordReader
import numpy as np
import plotly.graph_objects as go

reader = RecordReader("path/to/record.plm")
```

```python exec="on" session="record-parsing"
from plume import RecordReader
import numpy as np
import plotly.graph_objects as go

reader = RecordReader("docs/tutorials/beginner/basics/assets/record.plm")
```

With that done, we can now extract the position of the `Head` GameObject over time.

```python exec="on" source="above" linenums="1" session="record-parsing" title="Extracting the position of the head over time"
time_s = []
world_positions = []

# We iterate over all frames in the record file
for frame in reader.frames:
    # Scene containing the game object, in the Easter Egg Hunt demo it is called "HouseObjectivesSteamAudio"
    scene = frame.scenes.first_with_name("HouseObjectivesSteamAudio")

    # The scene may not exist in all frames, so we skip the frame if it is not found
    if scene is None:
        continue

    # Find the head GameObject in the scene
    head = scene.game_objects.first_with_name("Head") # (1)

    # The head may not exist in all frames, so we skip the frame if it is not found
    if head is None:
        continue
    
    # We extract its world position and append it to the arrays, along with the time
    world_position = head.transform.world_position
    world_positions.append(world_position)
    time_s.append(frame.time_s)

# Convert the lists to numpy arrays
time_s = np.array(time_s)
world_positions = np.array(world_positions)
```

1.  Note that multiple elements can have the same name, so the `first_with_name` function may not always return the desired element. We recommend using the GUID of the GameObject instead, and find it using `with_guid`.

We now have a timeseries of the player's head position. For sanity check, let's print the shape of our arrays, and the time range of the data.

```python exec="on" session="record-parsing" html="True"
# Replace fig.show() by hmtl output to display the plot in the page

def print_fig_html(fig):
    # center fig
    print("<center>")
    print(fig.to_html(full_html=False, include_plotlyjs="cdn"))
    print("</center>")

go.Figure.show = lambda fig: print_fig_html(fig)
```

```python exec="on" source="above" linenums="1" session="record-parsing" result="txt"
print(f"Time shape: {time_s.shape}")
print(f"World positions shape: {world_positions.shape}")
print(f"Time range: {time_s.min():.2f}s - {time_s.max():.2f}s")
```

We can now plot the trajectory of the player's head over time. Let's start by defining the function to plot the trajectory.

```python exec="on" source="above" linenums="1" session="record-parsing" title="Trajectory plotting function"
def plot_trajectory_3d(fig: go.Figure, positions: np.ndarray, time: np.ndarray, line_width: int = 5, cmap_name: str = "viridis"):
    fig.add_trace(
        go.Scatter3d(
            name="Path",
            x=positions[:, 0],
            y=positions[:, 2],
            z=positions[:, 1],
            # Add the time as custom data to be displayed in the hover tooltip
            customdata=time,
            line=dict(
                color=time,
                colorscale=cmap_name,
                width=line_width,
                colorbar=dict(title="Time (s)"),
            ),
            hovertemplate=
                '<b>X:</b> %{x:.2f}<br>' +
                '<b>Y:</b> %{y:.2f}<br>' +
                '<b>Z:</b> %{z:.2f}<br>' +
                '<b>Time:</b> %{customdata:.2f}s',
                mode="lines",
            )
    )
```

```python exec="on" source="above" linenums="1" session="record-parsing" title="Plotting the trajectory"

fig = go.Figure()

plot_trajectory_3d(fig, world_positions, time_s)

fig.update_layout(
    title="Player's head trajectory in world space over time (s)",
    # We swap the y and z axis to match the Unity coordinate system
    scene=dict(
        xaxis_title="X",
        yaxis_title="Z",
        zaxis_title="Y",
    ),
    width=800,
    height=800
)
fig.show()
```