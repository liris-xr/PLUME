
# common/color.proto



## Messages

### Color



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| r | float |  |  |
| g | float |  |  |
| b | float |  |  |
| a | float |  |  |



### ColorGradient



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| color_space | ColorSpace |  |  |
| mode | ColorGradient.GradientMode |  |  |
| color_keys | ColorGradient.ColorKey | repeated |  |
| alpha_keys | ColorGradient.AlphaKey | repeated |  |



### ColorGradient.AlphaKey



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| alpha | float |  |  |
| time | float |  |  |



### ColorGradient.ColorKey



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| color | Color |  |  |
| time | float |  |  |



 <!-- end of messages -->


## Enums

### ColorGradient.GradientMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| GRADIENT_MODE_BLEND | 0 |  |
| GRADIENT_MODE_FIXED | 1 |  |
| GRADIENT_MODE_PERCEPTUAL_BLEND | 2 |  |



### ColorSpace


| Name | Number | Description |
| ---- | ------ | ----------- |
| COLOR_SPACE_UNINITIALIZED | 0 |  |
| COLOR_SPACE_GAMMA | 1 |  |
| COLOR_SPACE_LINEAR | 2 |  |



 <!-- end of enums -->

 <!-- end of files -->