
# unity/transform.proto



## Messages

### TransformCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### TransformDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### TransformUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| parent_transform_id | ComponentIdentifier | optional |  |
| sibling_idx | int32 | optional |  |
| local_position | plume.sample.common.Vector3 | optional |  |
| local_rotation | plume.sample.common.Quaternion | optional |  |
| local_scale | plume.sample.common.Vector3 | optional |  |



 <!-- end of messages -->

 <!-- end of enums -->

 <!-- end of files -->