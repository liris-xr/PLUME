
# unity/line_renderer.proto



## Messages

### LineRendererCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### LineRendererDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### LineRendererUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| loop | bool | optional |  |
| width_curve | plume.sample.common.AnimationCurve | optional |  |
| width_multiplier | float | optional |  |
| positions | LineRendererUpdate.Positions | optional |  |
| color | plume.sample.common.ColorGradient | optional |  |
| corner_vertices | int32 | optional |  |
| end_cap_vertices | int32 | optional |  |
| alignment | Alignment | optional |  |
| texture_mode | TextureMode | optional |  |
| texture_scale | plume.sample.common.Vector2 | optional |  |
| shadow_bias | float | optional |  |
| generate_lighting_data | bool | optional |  |
| use_world_space | bool | optional |  |
| mask_interaction | MaskInteraction | optional |  |



### LineRendererUpdate.Positions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| positions | plume.sample.common.Vector3 | repeated |  |



 <!-- end of messages -->


## Enums

### Alignment


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALIGNMENT_VIEW | 0 |  |
| ALIGNMENT_TRANSFORM_Z | 1 |  |



### MaskInteraction


| Name | Number | Description |
| ---- | ------ | ----------- |
| MASK_INTERACTION_NONE | 0 |  |
| MASK_INTERACTION_VISIBLE_INSIDE | 1 |  |
| MASK_INTERACTION_VISIBLE_OUTSIDE | 2 |  |



### TextureMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| TEXTURE_MODE_STRETCH | 0 |  |
| TEXTURE_MODE_TILE | 1 |  |
| TEXTURE_MODE_DISTRIBUTE_PER_SEGMENT | 2 |  |
| TEXTURE_MODE_REPEAT_PER_SEGMENT | 3 |  |
| TEXTURE_MODE_STATIC | 4 |  |



 <!-- end of enums -->

 <!-- end of files -->