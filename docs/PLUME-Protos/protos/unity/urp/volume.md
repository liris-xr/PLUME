
# unity/urp/volume.proto



## Messages

### VolumeCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | plume.sample.unity.ComponentIdentifier |  |  |



### VolumeDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | plume.sample.unity.ComponentIdentifier |  |  |



### VolumeUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | plume.sample.unity.ComponentIdentifier |  |  |
| is_global | bool | optional |  |
| colliders | VolumeUpdate.Colliders | optional |  |
| blend_distance | float | optional |  |
| weight | float | optional |  |
| priority | float | optional |  |
| shared_profile_id | plume.sample.unity.AssetIdentifier | optional |  |



### VolumeUpdate.Colliders



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ids | plume.sample.unity.ComponentIdentifier | repeated |  |



### VolumeUpdateEnabled



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | plume.sample.unity.ComponentIdentifier |  |  |
| enabled | bool |  |  |



 <!-- end of messages -->

 <!-- end of enums -->

 <!-- end of files -->