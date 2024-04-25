# Usage

You can use PLUME Python from the terminal using the CLI or from your Python scripts.

### CLI

The CLI provides a set of commands to quickly extract data from the record files. You can use the `--help` option to get more information about the available commands and options.

```bash
Usage: plume-python [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.
  
Commands:
  export-csv               Export samples from the record to CSV files.
  export-world-transforms  Export world transforms of a GameObject with the given GUID to a CSV file.
  export-xdf               Export a XDF file including LSL samples and markers.
  find-guid                Find the GUID(s) of a GameObject by the given name.
  find-name                Find the name(s) of a GameObject with the given GUID in the record.
```

### API

To have more control over the data extraction process, you can use the PLUME Python API in your Python scripts. The following example shows a few common operations that you can perform using the API, for more information, you can refer to the API documentation in the related sections.

```python
import plume_python as plm
from plume_python.utils.dataframe import samples_to_dataframe, record_to_dataframes
from plume_python.samples.unity import transform_pb2
from plume_python.export import xdf_exporter 
from plume_python.utils.game_object import find_names_by_guid, find_first_identifier_by_name

# Load a record file
record = plm.parser.parse_record_from_file("path/to/record.plm")

# Find the name(s) of a game object by its GUID
names = find_names_by_guid(record, "4a3f40e37eaf4c0a9d5d88ac993c0ebc")

# Find the identifier (go + transform GUID) of a game object by its name
identifier = find_first_identifier_by_name(record, "MyGameObjectName")

# Get samples of a given type
transform_updates = record.get_samples_by_type(transform_pb2.TransformUpdate)

# Get samples in a given time range (in nanoseconds)
record.get_samples_in_time_range(0, 10_000)

# Get samples of a given type in a given time range (in nanoseconds)
record.get_samples_by_type_in_time_range(transform_pb2.TransformUpdate, 0, 10_000)

# Get sample absolute timestamp (in nanoseconds) since epoch
record.get_sample_timestamp_since_epoch(transform_updates[0])

# Convert samples to a pandas dataframe
transform_updates_df = samples_to_dataframe(transform_updates)

# Convert all samples to pandas dataframes
dataframes = record_to_dataframes(record)
transform_updates_df_2 = dataframes[transform_pb2.TransformUpdate]

# Export samples to a XDF file
with open("path/to/output.xdf", "wb") as xdf_file:
    xdf_exporter.export_xdf_from_record(xdf_file, record)
```