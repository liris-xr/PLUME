# Camera

A camera is a device through which the player views the world.

The `CameraRecorderModule` automatically picks up every camera in the scene and records:

- Near clip plane
- Far clip plane
- Field of view
- Rendering path
- Allow HDR
- Allow MSAA
- Allow dynamic resolution
- Force into render texture
- Orthographic
- Orthographic size
- Opaque sort mode
- Transparency sort mode
- Transparency sort axis
- Depth
- Aspect
- Culling mask
- Event mask
- Layer cull spherical
- Camera type
- Layer cull distances
- Use occlusion culling
- Culling matrix
- Background color
- Clear flags
- Depth texture mode
- Clear stencil after lighting pass
- Use physical properties
- Sensor size
- Lens shift
- Focal length
- Gate fit
- Rect
- Pixel rect
- Reference to target texture
- Target display
- World to camera matrix
- Projection matrix
- Non-jittered projection matrix
- Use jittered projection matrix for transparent rendering
- Stereo separation
- Stereo convergence
- Stereo target eye

## Creation and destruction

The creation and destruction of a camera are recorded as a [CameraCreate](../../advanced/format-specifications/unity/camera.md#cameracreate) and [CameraDestroy](../../advanced/format-specifications/unity/camera.md#cameradestroy) sample respectively.

When created, a [CameraUpdate](../../advanced/format-specifications/unity/camera.md#cameraupdate) sample is emitted with the initial properties of the camera.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../contributing.md).

!!! info
    See the [associated proto files](../../advanced/format-specifications/unity/camera.md) for more information on the data format.