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

Reading a record file is done using the `RecordReader` class. The reader provides methods to access the data in the record file easily. Each record file contains four main data streams:

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

