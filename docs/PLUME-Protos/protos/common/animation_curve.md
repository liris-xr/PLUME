
# common/animation_curve.proto



## Messages

### AnimationCurve



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| keyframes | AnimationCurveKeyFrame | repeated |  |



### AnimationCurveKeyFrame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time | float |  |  |
| value | float |  |  |
| in_tangent | float |  |  |
| out_tangent | float |  |  |
| weighted_mode | WeightedMode |  |  |
| in_weight | float |  |  |
| out_weight | float |  |  |



 <!-- end of messages -->


## Enums

### WeightedMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| WEIGHTED_MODE_NONE | 0 |  |
| WEIGHTED_MODE_IN | 1 |  |
| WEIGHTED_MODE_OUT | 2 |  |
| WEIGHTED_MODE_BOTH | 3 |  |



 <!-- end of enums -->

 <!-- end of files -->