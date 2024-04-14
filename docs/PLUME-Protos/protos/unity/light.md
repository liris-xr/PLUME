
# unity/light.proto



## Messages

### LayerShadowCullDistances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| distances | float | repeated |  |



### LightCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### LightDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### LightUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| enabled | bool | optional |  |
| type | LightType | optional |  |
| shape | LightShape | optional |  |
| intensity | float | optional |  |
| bounce_intensity | float | optional |  |
| range | float | optional |  |
| color | plume.sample.common.Color | optional |  |
| color_temperature | float | optional |  |
| use_color_temperature | bool | optional |  |
| spot_angle | float | optional |  |
| inner_spot_angle | float | optional |  |
| shadows | LightShadows | optional |  |
| shadow_strength | float | optional |  |
| shadow_resolution | LightShadowResolution | optional |  |
| shadow_matrix_override | plume.sample.common.Matrix4x4 | optional |  |
| use_shadow_matrix_override | bool | optional |  |
| shadow_bias | float | optional |  |
| shadow_normal_bias | float | optional |  |
| shadow_near_plane | float | optional |  |
| use_view_frustum_for_shadow_caster_cull | bool | optional |  |
| layer_shadow_cull_distances | LayerShadowCullDistances | optional | Only for directional lights |
| shadow_custom_resolution | int32 | optional | Only for Built-in RP |
| light_shadow_caster_mode | LightShadowCasterMode | optional | Not supported on legacy renderers |
| rendering_layer_mask | int32 | optional |  |
| culling_mask | int32 | optional |  |
| bounding_sphere_override | plume.sample.common.Vector4 | optional |  |
| use_bounding_sphere_override | bool | optional |  |
| cookie_id | AssetIdentifier | optional |  |
| cookie_size | float | optional |  |
| flare_id | AssetIdentifier | optional |  |



 <!-- end of messages -->


## Enums

### LightShadowCasterMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| LIGHT_SHADOW_CASTER_MODE_DEFAULT | 0 |  |
| LIGHT_SHADOW_CASTER_MODE_NON_LIGHTMAPPED_ONLY | 1 |  |
| LIGHT_SHADOW_CASTER_MODE_EVERYTHING | 2 |  |



### LightShadowResolution


| Name | Number | Description |
| ---- | ------ | ----------- |
| LIGHT_SHADOW_RESOLUTION_FROM_QUALITY_SETTINGS | 0 |  |
| LIGHT_SHADOW_RESOLUTION_LOW | 1 |  |
| LIGHT_SHADOW_RESOLUTION_MEDIUM | 2 |  |
| LIGHT_SHADOW_RESOLUTION_HIGH | 3 |  |
| LIGHT_SHADOW_RESOLUTION_VERY_HIGH | 4 |  |



### LightShadows


| Name | Number | Description |
| ---- | ------ | ----------- |
| LIGHT_SHADOWS_NONE | 0 |  |
| LIGHT_SHADOWS_HARD | 1 |  |
| LIGHT_SHADOWS_SOFT | 2 |  |



### LightShape


| Name | Number | Description |
| ---- | ------ | ----------- |
| LIGHT_SHAPE_CONE | 0 |  |
| LIGHT_SHAPE_PYRAMID | 1 |  |
| LIGHT_SHAPE_BOX | 2 |  |



### LightType


| Name | Number | Description |
| ---- | ------ | ----------- |
| LIGHT_TYPE_SPOT | 0 |  |
| LIGHT_TYPE_DIRECTIONAL | 1 |  |
| LIGHT_TYPE_POINT | 2 |  |
| LIGHT_TYPE_AREA | 3 |  |
| LIGHT_TYPE_RECTANGLE | 4 |  |
| LIGHT_TYPE_DISC | 5 |  |



 <!-- end of enums -->

 <!-- end of files -->