
# lsl/lsl_stream.proto



## Messages

### StreamClose



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stream_id | string |  | Unique identifier of the stream used by the recorder To get the session id, uid and source id, use the xml_header provided in the StreamOpen sample |



### StreamOpen



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stream_id | string |  | Unique identifier of the stream used by the recorder To get the session id, uid and source id, use the xml_header |
| xml_header | string |  | XML header containing: name, type, channel count, nominal sampling rate, etc. Cf. https://github.com/sccn/xdf/wiki/Specifications#streamheader-chunk |



### StreamSample



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stream_id | string |  | Unique identifier of the stream used by the recorder To get the session id, uid and source id, use the xml_header provided in the StreamOpen sample |
| float_values | StreamSample.RepeatedFloat |  |  |
| double_values | StreamSample.RepeatedDouble |  |  |
| string_values | StreamSample.RepeatedString |  |  |
| int8_values | StreamSample.RepeatedInt8 |  |  |
| int16_values | StreamSample.RepeatedInt16 |  |  |
| int32_values | StreamSample.RepeatedInt32 |  |  |
| int64_values | StreamSample.RepeatedInt64 |  |  |



### StreamSample.RepeatedDouble



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | double | repeated |  |



### StreamSample.RepeatedFloat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | float | repeated |  |



### StreamSample.RepeatedInt16



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | int32 | repeated |  |



### StreamSample.RepeatedInt32



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | int32 | repeated |  |



### StreamSample.RepeatedInt64



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | int64 | repeated |  |



### StreamSample.RepeatedInt8



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | int32 | repeated |  |



### StreamSample.RepeatedString



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | string | repeated |  |



 <!-- end of messages -->

 <!-- end of enums -->

 <!-- end of files -->