# Reading custom data

!!! info
    This page is a continuation of the [recording custom data](../../recorder/advanced/recording-custom-data.md) page. Make sure to read it before continuing.

After recording custom data with the PLUME Recorder, you can read it using the PLUME Python API. Let's start by compiling our custom message to Python.

## 1. Compiling the `.proto` file to Python

Assuming you followed the [recording custom data](../../recorder/advanced/recording-custom-data.md) guide, you should have `protoc` already installed. To compile your `.proto` file to Python, run the following command:

```bash
protoc --python_out=outputFolderName ./person.proto
```

This will generate a `person_pb2.py` file in the `outputFolderName` directory. You can now use this file to read your custom data.

## 2. Reading custom data

To read the custom data using the `plume_python` package, you will need to import the generated `person_pb2` file and use the `plume_python` API to load the record file then extract the custom data:

```python
import plume_python as plm
from plume_python.utils.dataframe import samples_to_dataframe, record_to_dataframes

# Import the generated proto file
import person_pb2

# Load a record file
record = plm.parser.parse_record_from_file("path/to/record.plm")

# Get samples of a given type
person_samples = record.get_samples_by_type(person_pb2.Person)

# Get samples of a given type in a given time range (in nanoseconds)
record.get_samples_by_type_in_time_range(person_pb2.Person, 0, 10_000)

# Get sample absolute timestamp (in nanoseconds) since epoch for the first sample
record.get_sample_timestamp_since_epoch(person_samples[0])

# Convert samples to a pandas dataframe
person_samples_df = samples_to_dataframe(person_samples)
```