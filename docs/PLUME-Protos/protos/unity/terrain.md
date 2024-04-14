
# unity/terrain.proto



## Messages

### TerrainCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### TerrainDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### TerrainUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| enabled | bool | optional |  |
| terrain_data_id | AssetIdentifier | optional |  |
| tree_distance | float | optional |  |
| tree_billboard_distance | float | optional |  |
| tree_cross_fade_length | float | optional |  |
| tree_maximum_full_lod_count | int32 | optional |  |
| detail_object_distance | float | optional |  |
| detail_object_density | float | optional |  |
| heightmap_pixel_error | float | optional |  |
| heightmap_maximum_lod | int32 | optional |  |
| basemap_distance | float | optional |  |
| lightmap_index | int32 | optional |  |
| realtime_lightmap_index | int32 | optional |  |
| lightmap_scale_offset | plume.sample.common.Vector4 | optional |  |
| realtime_lightmap_scale_offset | plume.sample.common.Vector4 | optional |  |
| keep_unused_rendering_resources | bool | optional |  |
| shadow_casting_mode | ShadowCastingMode | optional |  |
| reflection_probe_usage | ReflectionProbeUsage | optional |  |
| material_template_id | AssetIdentifier | optional |  |
| draw_heightmap | bool | optional |  |
| allow_auto_connect | bool | optional |  |
| grouping_id | int32 | optional |  |
| draw_instanced | bool | optional |  |
| normalmap_texture_id | AssetIdentifier | optional |  |
| draw_trees_and_foliage | bool | optional |  |
| patch_bounds_multiplier | plume.sample.common.Vector3 | optional |  |
| tree_lod_bias_multiplier | float | optional |  |
| collect_detail_patches | bool | optional |  |



 <!-- end of messages -->

 <!-- end of enums -->

 <!-- end of files -->