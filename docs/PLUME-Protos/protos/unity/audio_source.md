
# unity/audio_source.proto



## Messages

### AudioSourceCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### AudioSourceDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### AudioSourceUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| audio_clip_id | AssetIdentifier | optional |  |
| audio_mixer_group_id | AssetIdentifier | optional |  |
| is_playing | bool | optional |  |
| time_samples | int32 | optional |  |
| mute | bool | optional |  |
| bypass_effects | bool | optional |  |
| bypass_listener_effects | bool | optional |  |
| bypass_reverb_zones | bool | optional |  |
| priority | int32 | optional |  |
| volume | float | optional |  |
| pitch | float | optional |  |
| stereo_pan | float | optional |  |
| spatial_blend | plume.sample.common.AnimationCurve | optional |  |
| reverb_zone_mix | plume.sample.common.AnimationCurve | optional |  |
| doppler_level | float | optional |  |
| spread | plume.sample.common.AnimationCurve | optional |  |
| volume_rolloff | plume.sample.common.AnimationCurve | optional |  |



 <!-- end of messages -->

 <!-- end of enums -->

 <!-- end of files -->