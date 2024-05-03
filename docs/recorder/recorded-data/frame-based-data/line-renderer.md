# Line Renderer

The line renderer is a component that renders a line or a series of connected lines.

The `LineRendererRecorderModule` automatically picks up every line renderer in the scene and records:

- Whether the line renderer is enabled or not
- Whether the line renderer is using the world space or the local space
- Whether the line renderer is looping or not
- Positions of the line points
- Width (as key points)
- Color (as key points/color gradient)
- Number of corner vertices
- Number of end cap vertices
- Alignment
- Texture mode
- Shadow bias

## Creation and destruction

The creation and destruction of a line renderer component are recorded as a [LineRendererCreate](../../file-format/proto-files/unity/line_renderer.md#linerenderercreate) and [LineRendererDestroy](../../file-format/proto-files/unity/line_renderer.md#linerendererdestroy) sample respectively.

When created, a [LineRendererUpdate](../../file-format/proto-files/unity/line_renderer.md#linerendererupdate) sample is emitted with the initial values of the line renderer component.

## Update

### Hooks

A [LineRendererUpdate](../../file-format/proto-files/unity/line_renderer.md#linerendererupdate) sample is emitted when a change in the component properties is detected. The following methods are hooked to detect those changes:

- [Renderer.enabled](https://docs.unity3d.com/ScriptReference/Renderer-enabled.html)
- [Renderer.material](https://docs.unity3d.com/ScriptReference/Renderer-material.html)
- [Renderer.materials](https://docs.unity3d.com/ScriptReference/Renderer-materials.html)
- [Renderer.sharedMaterial](https://docs.unity3d.com/ScriptReference/Renderer-sharedMaterial.html)
- [Renderer.sharedMaterials](https://docs.unity3d.com/ScriptReference/Renderer-sharedMaterials.html)
- [void Renderer.SetPropertyBlock(MaterialPropertyBlock properties)](https://docs.unity3d.com/ScriptReference/Renderer.SetPropertyBlock.html)
- [void Renderer.SetPropertyBlock(MaterialPropertyBlock properties, int materialIndex)](https://docs.unity3d.com/ScriptReference/Renderer.SetPropertyBlock.html)
- [LineRenderer.widthMultiplier](https://docs.unity3d.com/ScriptReference/LineRenderer-widthMultiplier.html)
- [LineRenderer.startWidth](https://docs.unity3d.com/ScriptReference/LineRenderer-startWidth.html)
- [LineRenderer.endWidth](https://docs.unity3d.com/ScriptReference/LineRenderer-endWidth.html)
- [LineRenderer.widthCurve](https://docs.unity3d.com/ScriptReference/LineRenderer-widthCurve.html)
- [LineRenderer.startColor](https://docs.unity3d.com/ScriptReference/LineRenderer-startColor.html)
- [LineRenderer.endColor](https://docs.unity3d.com/ScriptReference/LineRenderer-endColor.html)
- [LineRenderer.colorGradient](https://docs.unity3d.com/ScriptReference/LineRenderer-colorGradient.html)
- [LineRenderer.positionCount](https://docs.unity3d.com/ScriptReference/LineRenderer-positionCount.html)
- [LineRenderer.SetPosition(int index, Vector3 position)](https://docs.unity3d.com/ScriptReference/LineRenderer.SetPosition.html)
- [LineRenderer.SetPositions(Vector3[] positions)](https://docs.unity3d.com/ScriptReference/LineRenderer.SetPositions.html)
- [LineRenderer.SetPositions(NativeArray<Vector3> positions)](https://docs.unity3d.com/ScriptReference/LineRenderer.SetPositions.html)
- [LineRenderer.SetPositions(NativeSlice<Vector3> positions)](https://docs.unity3d.com/ScriptReference/LineRenderer.SetPositions.html)

!!! info
    See the [associated proto files](../../file-format/proto-files/unity/line_renderer.md) for more information on the data format.
