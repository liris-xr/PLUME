# Record

Each record file starts with a timeless [RecordMetadata](../../file-format/proto-files/record.md#recordmetadata) sample containing:

- The version of the recorder as a [RecorderVersion](../../file-format/proto-files/record.md#recorderversion) sample.
- The UNIX start time of the record (in seconds) since epoch. As [timestamps](../../timestamps.md) in the record files are expressed relatively to the start of the recorder in nanoseconds, this start time since epoch is useful if you want to get an absolute time.
- The name of the record, as defined in the [recorder global settings](../../global-settings.md#global-settings) or in the call to `StartRecording`.
- Extra metadata, as defined in the [recorder global settings](../../global-settings.md#global-settings) or in the call to `StartRecording`.
