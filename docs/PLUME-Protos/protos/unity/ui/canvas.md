
# unity/ui/canvas.proto



## Messages

### CanvasCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### CanvasDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### CanvasUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| render_mode | RenderMode | optional |  |
| scale_factor | float | optional |  |
| reference_pixels_per_unit | float | optional |  |
| override_pixel_perfect | bool | optional |  |
| vertex_color_always_gamma_space | bool | optional |  |
| pixel_perfect | bool | optional |  |
| plane_distance | float | optional |  |
| override_sorting | bool | optional |  |
| sorting_order | int32 | optional |  |
| target_display | int32 | optional |  |
| sorting_layer_id | int32 | optional |  |
| additional_shader_channels | uint32 | optional |  |
| sorting_layer_name | string | optional |  |
| update_rect_transform_for_standalone | StandaloneRenderResize | optional |  |
| world_camera | ComponentIdentifier | optional |  |
| normalized_sorting_grid_size | float | optional |  |



 <!-- end of messages -->


## Enums

### RenderMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| RENDER_MODE_SCREEN_SPACE_OVERLAY | 0 |  |
| RENDER_MODE_SCREEN_SPACE_CAMERA | 1 |  |
| RENDER_MODE_WORLD_SPACE | 2 |  |



### StandaloneRenderResize


| Name | Number | Description |
| ---- | ------ | ----------- |
| STANDALONE_RENDER_RESIZE_ENABLED | 0 |  |
| STANDALONE_RENDER_RESIZE_DISABLED | 1 |  |



 <!-- end of enums -->

 <!-- end of files -->