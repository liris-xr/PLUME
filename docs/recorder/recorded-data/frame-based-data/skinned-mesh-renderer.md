# Skinned Mesh Renderer

The skinned mesh renderer is a component that renders meshes that are deformed by bones. It is used for characters and other objects that need to be animated.

The `SkinnedMeshRendererRecorderModule` automatically picks up every skinned mesh renderer in the scene and records:

- Whether the skinned mesh renderer is enabled or not
- Reference to the mesh asset
- Reference to the materials assets
- Reference to the root bone
- Reference to the bones
- Blend shape weights

## Creation and destruction

The creation and destruction of a skinned mesh renderer component are recorded as a [SkinnedMeshRendererCreate](../../advanced/format-specifications/unity/skinned_mesh_renderer.md#skinnedmeshrenderercreate) and [SkinnedMeshRendererDestroy](../../advanced/format-specifications/unity/skinned_mesh_renderer.md#skinnedmeshrendererdestroy) sample respectively.

When created, a [SkinnedMeshRendererUpdate](../../advanced/format-specifications/unity/skinned_mesh_renderer.md#skinnedmeshrendererupdate) and [RendererUpdate](../../advanced/format-specifications/unity/renderer.md#rendererupdate) samples are emitted with the initial values of the skinned mesh renderer component.

## Update

### Hooks

A [SkinnedMeshRendererUpdate](../../advanced/format-specifications/unity/skinned_mesh_renderer.md#skinnedmeshrendererupdate) sample is emitted when a change in the component properties is detected. The following methods are hooked to detect those changes:

- [Renderer.enabled](https://docs.unity3d.com/ScriptReference/Renderer-enabled.html)
- [Renderer.material](https://docs.unity3d.com/ScriptReference/Renderer-material.html)
- [Renderer.materials](https://docs.unity3d.com/ScriptReference/Renderer-materials.html)
- [Renderer.sharedMaterial](https://docs.unity3d.com/ScriptReference/Renderer-sharedMaterial.html)
- [Renderer.sharedMaterials](https://docs.unity3d.com/ScriptReference/Renderer-sharedMaterials.html)
- [void Renderer.SetPropertyBlock(MaterialPropertyBlock properties)](https://docs.unity3d.com/ScriptReference/Renderer.SetPropertyBlock.html)
- [void Renderer.SetPropertyBlock(MaterialPropertyBlock properties, int materialIndex)](https://docs.unity3d.com/ScriptReference/Renderer.SetPropertyBlock.html)
- [void Renderer.SetMaterials(List<Material> materials)](https://docs.unity3d.com/ScriptReference/Renderer.SetMaterials.html)
- [void Renderer.SetSharedMaterials(List<Material> materials)](https://docs.unity3d.com/ScriptReference/Renderer.SetSharedMaterials.html)
- [SkinnedMeshRenderer.bones](https://docs.unity3d.com/ScriptReference/SkinnedMeshRenderer-bones.html)
- [SkinnedMeshRenderer.rootBone](https://docs.unity3d.com/ScriptReference/SkinnedMeshRenderer-rootBone.html)
- [SkinnedMeshRenderer.SetBlendShapeWeight(int index, float value)](https://docs.unity3d.com/ScriptReference/SkinnedMeshRenderer.SetBlendShapeWeight.html)

!!! info
    See the [associated proto files](../../advanced/format-specifications/unity/skinned_mesh_renderer.md) for more information on the data format.