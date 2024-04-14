
# unity/identifiers.proto



## Messages

### AssetIdentifier



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | string |  |  |
| path | string |  |  |



### ComponentIdentifier



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| component_id | string |  |  |
| parent_id | GameObjectIdentifier |  |  |



### GameObjectIdentifier



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_object_id | string |  |  |
| transform_id | string |  |  |



### SceneIdentifier



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | string |  |  |
| runtime_index | string |  |  |
| name | string |  |  |
| path | string |  |  |
| build_index | int32 |  |  |
| mode | LoadSceneMode |  |  |



 <!-- end of messages -->


## Enums

### LoadSceneMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| LOAD_SCENE_MODE_SINGLE | 0 |  |
| LOAD_SCENE_MODE_ADDITIVE | 1 |  |



 <!-- end of enums -->

 <!-- end of files -->