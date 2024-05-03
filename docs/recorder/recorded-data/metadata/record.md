# Record

Metadata about the record itself is recorded at the beginning of each recording. This metadata includes:

- The version of the recorder.
- The UNIX start time of the record (in seconds) since epoch.

    !!! tip
        As [timestamps](../../advanced/timestamps.md) in the record files are expressed relatively to the start of the recorder in nanoseconds, this start time since epoch is useful if you want to get an absolute time for the samples.

- The name of the record, as defined in the [recorder global settings](../../global-settings.md#global-settings) or in the call to `StartRecording`.
- Extra metadata, as defined in the [recorder global settings](../../global-settings.md#global-settings) or in the call to `StartRecording`.

!!! info
    See the [associated proto file](../../advanced/format-specifications/record.md#recordmetadata) for more information on the data format.