
# unity/urp/additional_camera_data.proto



## Messages

### AdditionalCameraDataCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | plume.sample.unity.ComponentIdentifier |  |  |



### AdditionalCameraDataDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | plume.sample.unity.ComponentIdentifier |  |  |



### AdditionalCameraDataUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | plume.sample.unity.ComponentIdentifier |  |  |
| version | float | optional |  |
| render_shadows | bool | optional |  |
| requires_depth_option | CameraOverrideOption | optional |  |
| requires_color_option | CameraOverrideOption | optional |  |
| render_type | CameraRenderType | optional |  |
| requires_depth_texture | bool | optional |  |
| requires_color_texture | bool | optional |  |
| volume_layer_mask | int32 | optional |  |
| volume_trigger_id | plume.sample.unity.ComponentIdentifier | optional |  |
| render_post_processing | bool | optional |  |
| antialiasing | AntialiasingMode | optional |  |
| antialiasing_quality | AntialiasingQuality | optional |  |
| stop_nan | bool | optional |  |
| dithering | bool | optional |  |
| allow_xr_rendering | bool | optional |  |



 <!-- end of messages -->


## Enums

### CameraOverrideOption


| Name | Number | Description |
| ---- | ------ | ----------- |
| CAMERA_OVERRIDE_OPTION_OFF | 0 |  |
| CAMERA_OVERRIDE_OPTION_ON | 1 |  |
| CAMERA_OVERRIDE_OPTION_USE_PIPELINE_SETTINGS | 2 |  |



### CameraRenderType


| Name | Number | Description |
| ---- | ------ | ----------- |
| CAMERA_RENDER_TYPE_BASE | 0 |  |
| CAMERA_RENDER_TYPE_OVERLAY | 1 |  |



 <!-- end of enums -->

 <!-- end of files -->