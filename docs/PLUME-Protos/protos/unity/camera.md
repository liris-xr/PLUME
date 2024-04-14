
# unity/camera.proto



## Messages

### CameraCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### CameraDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### CameraLayerCullDistances



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| distances | float | repeated |  |



### CameraUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| near_clip_plane | float | optional |  |
| far_clip_plane | float | optional |  |
| field_of_view | float | optional |  |
| rendering_path | RenderingPath | optional |  |
| allow_hdr | bool | optional |  |
| allow_msaa | bool | optional |  |
| allow_dynamic_resolution | bool | optional |  |
| force_into_render_texture | bool | optional |  |
| orthographic_size | float | optional |  |
| orthographic | bool | optional |  |
| opaque_sort_mode | OpaqueSortMode | optional |  |
| transparency_sort_mode | TransparencySortMode | optional |  |
| transparency_sort_axis | plume.sample.common.Vector3 | optional |  |
| depth | float | optional |  |
| aspect | float | optional |  |
| culling_mask | int32 | optional |  |
| event_mask | int32 | optional |  |
| layer_cull_spherical | bool | optional |  |
| camera_type | uint32 | optional |  |
| layer_cull_distances | CameraLayerCullDistances | optional |  |
| use_occlusion_culling | bool | optional |  |
| culling_matrix | plume.sample.common.Matrix4x4 | optional |  |
| background_color | plume.sample.common.Color | optional |  |
| clear_flags | uint32 | optional |  |
| depth_texture_mode | uint32 | optional |  |
| clear_stencil_after_lighting_pass | bool | optional |  |
| use_physical_properties | bool | optional |  |
| sensor_size | plume.sample.common.Vector2 | optional |  |
| lens_shift | plume.sample.common.Vector2 | optional |  |
| focal_length | float | optional |  |
| gate_fit | CameraGateFitMode | optional |  |
| rect | plume.sample.common.Rect | optional |  |
| pixel_rect | plume.sample.common.Rect | optional |  |
| target_texture_id | AssetIdentifier | optional |  |
| target_display | int32 | optional |  |
| world_to_camera_matrix | plume.sample.common.Matrix4x4 | optional |  |
| projection_matrix | plume.sample.common.Matrix4x4 | optional |  |
| non_jittered_projection_matrix | plume.sample.common.Matrix4x4 | optional |  |
| use_jittered_projection_matrix_for_transparent_rendering | bool | optional |  |
| stereo_separation | float | optional |  |
| stereo_convergence | float | optional |  |
| stereo_target_eye | CameraStereoTargetEyeMask | optional |  |



 <!-- end of messages -->


## Enums

### CameraGateFitMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| CAMERA_GATE_FIT_MODE_NONE | 0 |  |
| CAMERA_GATE_FIT_MODE_VERTICAL | 1 |  |
| CAMERA_GATE_FIT_MODE_HORIZONTAL | 2 |  |
| CAMERA_GATE_FIT_MODE_FILL | 3 |  |
| CAMERA_GATE_FIT_MODE_OVERSCAN | 4 |  |



### CameraStereoTargetEyeMask


| Name | Number | Description |
| ---- | ------ | ----------- |
| CAMERA_STEREO_TARGET_EYE_MASK_NONE | 0 |  |
| CAMERA_STEREO_TARGET_EYE_MASK_LEFT | 1 |  |
| CAMERA_STEREO_TARGET_EYE_MASK_RIGHT | 2 |  |
| CAMERA_STEREO_TARGET_EYE_MASK_BOTH | 3 |  |



 <!-- end of enums -->

 <!-- end of files -->