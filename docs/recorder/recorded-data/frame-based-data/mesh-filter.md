# Mesh Filter

The mesh filter is a component that stores a reference to a mesh asset. It is used by the MeshRenderer component to render a mesh.

The `MeshFilterRecorderModule` automatically picks up every mesh filter in the scene and records:

- Reference to the mesh asset

## Creation and destruction

The creation and destruction of a mesh filter component are recorded as a [MeshFilterCreate](../../advanced/format-specifications/unity/mesh_filter.md#meshfiltercreate) and [MeshFilterDestroy](../../advanced/format-specifications/unity/mesh_filter.md#meshfilterdestroy) sample respectively.

When created, a [MeshFilterUpdate](../../advanced/format-specifications/unity/mesh_filter.md#meshfilterupdate) sample is emitted with the initial values of the mesh filter component.

## Update

### Hooks

A [MeshFilterUpdate](../../advanced/format-specifications/unity/mesh_filter.md#meshfilterupdate) sample is emitted when a change in the component properties is detected. The following methods are hooked to detect those changes:

- [MeshFilter.mesh (setter)](https://docs.unity3d.com/ScriptReference/MeshFilter-mesh.html)
- [MeshFilter.mesh (getter)](https://docs.unity3d.com/ScriptReference/MeshFilter-mesh.html)

    !!! info
        Unity instantiate a duplicate of the mesh when the getter is queried for the first time. By hooking the getter, we can record the new mesh asset reference.

- [MeshFilter.sharedMesh](https://docs.unity3d.com/ScriptReference/MeshFilter-sharedMesh.html)

!!! info
    See the [associated proto files](../../advanced/format-specifications/unity/mesh_filter.md) for more information on the data format.
