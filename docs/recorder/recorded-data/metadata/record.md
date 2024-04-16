# Record

Each record file starts with timeless [RecordMetadata](../../file-format/proto-files/record.md#recordmetadata) sample containing:

- The version of the recorder
- The UNIX start time of the record (in seconds) since epoch
- The name of the record, as defined in the [recorder global settings](../../global-settings.md#global-settings) or in the call to `StartRecording`.
- Extra metadata, as defined in the [recorder global settings](../../global-settings.md#global-settings) or in the call to `StartRecording`.
