
# unity/skinned_mesh_renderer.proto



## Messages

### SkinnedMeshRendererCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### SkinnedMeshRendererDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### SkinnedMeshRendererUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| mesh_id | AssetIdentifier | optional |  |
| root_bone_id | ComponentIdentifier | optional |  |
| bones | SkinnedMeshRendererUpdate.Bones | optional |  |
| blend_shape_weights | SkinnedMeshRendererUpdate.BlendShapeWeights | optional |  |



### SkinnedMeshRendererUpdate.BlendShapeWeights



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| weights | SkinnedMeshRendererUpdate.BlendShapeWeights.BlendShapeWeight | repeated |  |



### SkinnedMeshRendererUpdate.BlendShapeWeights.BlendShapeWeight



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | int32 |  |  |
| weight | float |  |  |



### SkinnedMeshRendererUpdate.Bones



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ids | ComponentIdentifier | repeated |  |



 <!-- end of messages -->

 <!-- end of enums -->

 <!-- end of files -->