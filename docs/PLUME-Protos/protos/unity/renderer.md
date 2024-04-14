
# unity/renderer.proto



## Messages

### RendererUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| enabled | bool | optional |  |
| materials | RendererUpdate.Materials | optional |  |
| local_bounds | plume.sample.common.Bounds | optional |  |
| lightmap_index | int32 | optional |  |
| lightmap_scale_offset | plume.sample.common.Vector4 | optional |  |
| realtime_lightmap_index | int32 | optional |  |
| realtime_lightmap_scale_offset | plume.sample.common.Vector4 | optional |  |



### RendererUpdate.Materials



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ids | AssetIdentifier | repeated |  |



 <!-- end of messages -->

 <!-- end of enums -->

 <!-- end of files -->