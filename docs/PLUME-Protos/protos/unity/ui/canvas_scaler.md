
# unity/ui/canvas_scaler.proto



## Messages

### CanvasScalerCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### CanvasScalerDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### CanvasScalerUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| ui_scale_mode | ScaleMode | optional |  |
| reference_pixels_per_unit | float | optional |  |
| scale_factor | float | optional |  |
| reference_resolution | plume.sample.common.Vector2 | optional |  |
| screen_match_mode | ScreenMatchMode | optional |  |
| match_width_or_height | float | optional |  |
| physical_unit | Unit | optional |  |
| fallback_screen_dpi | float | optional |  |
| default_sprite_dpi | float | optional |  |
| dynamic_pixels_per_unit | float | optional |  |



 <!-- end of messages -->


## Enums

### ScaleMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| SCALE_MODE_CONSTANT_PIXEL_SIZE | 0 |  |
| SCALE_MODE_SCALE_WITH_SCREEN_SIZE | 1 |  |
| SCALE_MODE_CONSTANT_PHYSICAL_SIZE | 2 |  |



### ScreenMatchMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| SCREEN_MATCH_MODE_MATCH_WIDTH_OR_HEIGHT | 0 |  |
| SCREEN_MATCH_MODE_EXPAND | 1 |  |
| SCREEN_MATCH_MODE_SHRINK | 2 |  |



### Unit


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNIT_CENTIMETERS | 0 |  |
| UNIT_MILLIMETERS | 1 |  |
| UNIT_INCHES | 2 |  |
| UNIT_POINTS | 3 |  |
| UNIT_PICAS | 4 |  |



 <!-- end of enums -->

 <!-- end of files -->