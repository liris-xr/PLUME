
# unity/xritk/input_action.proto



## Messages

### ButtonValue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| boolean | bool |  |  |
| float | float |  |  |
| threshold | float |  |  |



### InputAction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | plume.sample.unity.ComponentIdentifier |  |  |
| name | string |  |  |
| binding_paths | string | repeated |  |
| type | InputActionType |  |  |
| boolean | bool |  |  |
| integer | int32 |  |  |
| float | float |  |  |
| double | double |  |  |
| vector2 | plume.sample.common.Vector2 |  |  |
| vector3 | plume.sample.common.Vector3 |  |  |
| quaternion | plume.sample.common.Quaternion |  |  |
| button | ButtonValue |  |  |



 <!-- end of messages -->


## Enums

### InputActionType


| Name | Number | Description |
| ---- | ------ | ----------- |
| VALUE | 0 |  |
| BUTTON | 1 |  |
| PASSTHROUGH | 2 |  |



 <!-- end of enums -->

 <!-- end of files -->