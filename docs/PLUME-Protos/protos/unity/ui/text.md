
# unity/ui/text.proto



## Messages

### TextCreate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### TextDestroy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |



### TextUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | ComponentIdentifier |  |  |
| text | string | optional |  |
| font_id | AssetIdentifier | optional |  |
| font_style | FontStyle | optional |  |
| font_size | int32 | optional |  |
| color | plume.sample.common.Color | optional |  |
| line_spacing | float | optional |  |
| support_rich_text | bool | optional |  |
| alignment | TextAnchor | optional |  |
| align_by_geometry | bool | optional |  |
| horizontal_overflow | HorizontalWrapMode | optional |  |
| vertical_overflow | VerticalWrapMode | optional |  |
| resize_text_for_best_fit | bool | optional |  |
| resize_text_min_size | int32 | optional |  |
| resize_text_max_size | int32 | optional |  |



 <!-- end of messages -->


## Enums

### FontStyle


| Name | Number | Description |
| ---- | ------ | ----------- |
| FONT_STYLE_NORMAL | 0 |  |
| FONT_STYLE_BOLD | 1 |  |
| FONT_STYLE_ITALIC | 2 |  |
| FONT_STYLE_BOLD_AND_ITALIC | 3 |  |



### HorizontalWrapMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| HORIZONTAL_WRAP_MODE_WRAP | 0 |  |
| HORIZONTAL_WRAP_MODE_OVERFLOW | 1 |  |



### TextAnchor


| Name | Number | Description |
| ---- | ------ | ----------- |
| TEXT_ANCHOR_UPPER_LEFT | 0 |  |
| TEXT_ANCHOR_UPPER_CENTER | 1 |  |
| TEXT_ANCHOR_UPPER_RIGHT | 2 |  |
| TEXT_ANCHOR_MIDDLE_LEFT | 3 |  |
| TEXT_ANCHOR_MIDDLE_CENTER | 4 |  |
| TEXT_ANCHOR_MIDDLE_RIGHT | 5 |  |
| TEXT_ANCHOR_LOWER_LEFT | 6 |  |
| TEXT_ANCHOR_LOWER_CENTER | 7 |  |
| TEXT_ANCHOR_LOWER_RIGHT | 8 |  |



### VerticalWrapMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| VERTICAL_WRAP_MODE_TRUNCATE | 0 |  |
| VERTICAL_WRAP_MODE_OVERFLOW | 1 |  |



 <!-- end of enums -->

 <!-- end of files -->