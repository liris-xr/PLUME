
# unity/ui/image.proto



## Messages

### ImageCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### ImageDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### ImageUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| sprite_id | AssetIdentifier | optional |  |
| type | ImageType | optional |  |



 <!-- end of messages -->


## Enums

### ImageType


| Name | Number | Description |
| ---- | ------ | ----------- |
| IMAGE_TYPE_SIMPLE | 0 |  |
| IMAGE_TYPE_SLICED | 1 |  |
| IMAGE_TYPE_TILED | 2 |  |
| IMAGE_TYPE_FILLED | 3 |  |



 <!-- end of enums -->

 <!-- end of files -->