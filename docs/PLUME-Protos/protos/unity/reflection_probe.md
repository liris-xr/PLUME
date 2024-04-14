
# unity/reflection_probe.proto



## Messages

### ReflectionProbeCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### ReflectionProbeDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### ReflectionProbeUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| enabled | bool | optional |  |
| mode | ReflectionProbeMode | optional |  |
| refresh_mode | ReflectionProbeRefreshMode | optional |  |
| time_slicing_mode | ReflectionProbeTimeSlicingMode | optional |  |
| clear_flags | ReflectionProbeClearFlags | optional |  |
| importance | int32 | optional |  |
| intensity | float | optional |  |
| near_clip_plane | float | optional |  |
| far_clip_plane | float | optional |  |
| render_dynamic_objects | bool | optional |  |
| box_projection | bool | optional |  |
| blend_distance | float | optional |  |
| bounds | plume.sample.common.Bounds | optional |  |
| resolution | int32 | optional |  |
| hdr | bool | optional |  |
| shadow_distance | float | optional |  |
| background_color | plume.sample.common.Color | optional |  |
| culling_mask | int32 | optional |  |
| custom_baked_texture_id | AssetIdentifier | optional |  |
| baked_texture_id | AssetIdentifier | optional |  |



 <!-- end of messages -->


## Enums

### ReflectionProbeClearFlags


| Name | Number | Description |
| ---- | ------ | ----------- |
| REFLECTION_PROBE_CLEAR_FLAGS_SKYBOX | 0 |  |
| REFLECTION_PROBE_CLEAR_FLAGS_SOLID_COLOR | 1 |  |



### ReflectionProbeMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| REFLECTION_PROBE_MODE_BAKED | 0 |  |
| REFLECTION_PROBE_MODE_CUSTOM | 1 |  |
| REFLECTION_PROBE_MODE_REALTIME | 2 |  |



### ReflectionProbeRefreshMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| REFLECTION_PROBE_REFRESH_MODE_ON_AWAKE | 0 |  |
| REFLECTION_PROBE_REFRESH_MODE_EVERY_FRAME | 1 |  |
| REFLECTION_PROBE_REFRESH_MODE_VIA_SCRIPTING | 2 |  |



### ReflectionProbeTimeSlicingMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| REFLECTION_PROBE_TIME_SLICING_MODE_ALL_FACES_AT_ONCE | 0 |  |
| REFLECTION_PROBE_TIME_SLICING_MODE_INDIVIDUAL_FACES | 1 |  |
| REFLECTION_PROBE_TIME_SLICING_MODE_NO_TIME_SLICING | 2 |  |



 <!-- end of enums -->

 <!-- end of files -->