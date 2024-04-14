
# record.proto



## Messages

### RecordMetadata



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| recorder_version | RecorderVersion |  |  |
| start_time | google.protobuf.Timestamp |  | Unix timestamp in seconds of when the recording started |
| name | string |  |  |
| extra_metadata | string |  |  |



### RecordMetrics



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| is_sequential | bool |  |  |
| duration | uint64 |  |  |
| n_samples | uint64 |  |  |



### RecorderVersion



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | string |  |  |
| major | string |  |  |
| minor | string |  |  |
| patch | string |  |  |



 <!-- end of messages -->

 <!-- end of enums -->

 <!-- end of files -->