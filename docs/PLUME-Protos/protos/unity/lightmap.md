
# unity/lightmap.proto



## Messages

### LightmapData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lightmap_color_texture_id | AssetIdentifier | optional |  |
| lightmap_dir_texture_id | AssetIdentifier | optional |  |
| lightmap_shadow_mask_texture_id | AssetIdentifier | optional |  |



### LightmapsUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lightmaps_mode | LightmapsMode |  |  |
| lightmaps_data | LightmapData | repeated |  |



 <!-- end of messages -->


## Enums

### LightmapsMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| LIGHTMAPS_MODE_NON_DIRECTIONAL | 0 |  |
| LIGHTMAPS_MODE_COMBINED_DIRECTIONAL | 1 |  |



 <!-- end of enums -->

 <!-- end of files -->