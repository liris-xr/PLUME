# Mesh Renderer

The mesh renderer is a component that renders a mesh.

The `MeshRendererRecorderModule` automatically picks up every mesh renderer in the scene and records:

- Whether the mesh renderer is enabled or not
- Reference to the mesh asset

## Creation and destruction

The creation and destruction of a mesh renderer component are recorded as a [MeshRendererCreate](../../advanced/format-specifications/unity/mesh_renderer.md#meshrenderercreate) and [MeshRendererDestroy](../../advanced/format-specifications/unity/mesh_renderer.md#meshrendererdestroy) sample respectively.

When created, a [MeshRendererUpdate](../../advanced/format-specifications/unity/mesh_renderer.md#meshrendererupdate) and [RendererUpdate](../../advanced/format-specifications/unity/renderer.md#rendererupdate) samples are emitted with the initial values of the mesh renderer component.

## Update

### Hooks

A [MeshRendererUpdate](../../advanced/format-specifications/unity/mesh_renderer.md#meshrendererupdate) sample is emitted when a change in the component properties is detected. The following methods are hooked to detect those changes:

- [Renderer.enabled](https://docs.unity3d.com/ScriptReference/Renderer-enabled.html)
- [Renderer.material](https://docs.unity3d.com/ScriptReference/Renderer-material.html)
- [Renderer.materials](https://docs.unity3d.com/ScriptReference/Renderer-materials.html)
- [Renderer.sharedMaterial](https://docs.unity3d.com/ScriptReference/Renderer-sharedMaterial.html)
- [Renderer.sharedMaterials](https://docs.unity3d.com/ScriptReference/Renderer-sharedMaterials.html)
- [void Renderer.SetPropertyBlock(MaterialPropertyBlock properties)](https://docs.unity3d.com/ScriptReference/Renderer.SetPropertyBlock.html)
- [void Renderer.SetPropertyBlock(MaterialPropertyBlock properties, int materialIndex)](https://docs.unity3d.com/ScriptReference/Renderer.SetPropertyBlock.html)
- [void Renderer.SetMaterials(List<Material> materials)](https://docs.unity3d.com/ScriptReference/Renderer.SetMaterials.html)
- [void Renderer.SetSharedMaterials(List<Material> materials)](https://docs.unity3d.com/ScriptReference/Renderer.SetSharedMaterials.html)

!!! info
    See the [associated proto files](../../advanced/format-specifications/unity/mesh_renderer.md) for more information on the data format.
