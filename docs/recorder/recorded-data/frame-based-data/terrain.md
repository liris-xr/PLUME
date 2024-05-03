# Terrain

Terrains are a special type of component in Unity that allows for the creation of large, detailed landscapes.

The `TerrainRecorderModule` automatically picks up every terrain in the scene and records:

- Reference to the terrain data asset
- Reference to the material template asset
- Tree distance
- Tree billboard distance
- Tree cross fade length
- Tree maximum full LOD count
- Detail object distance
- Detail object density
- Heightmap pixel error
- Heightmap maximum LOD
- Basemap distance
- Lightmap index
- Lightmap scale offset
- Realtime lightmap index
- Shadow casting mode
- Reflection probe usage
- Draw heightmap (bool)
- Allow auto connect (bool)
- Grouping ID
- Draw instanced (bool)
- Draw trees and foliage (bool)
- Patch bounds multiplier
- Tree LOD bias multiplier
- Collect detail patches (bool)

## Creation and destruction

The creation and destruction of a terrain component are recorded as a [TerrainCreate](../../file-format/proto-files/unity/terrain.md#terraincreate) and [TerrainDestroy](../../file-format/proto-files/unity/terrain.md#terraindestroy) sample respectively.

When created, a [TerrainUpdate](../../file-format/proto-files/unity/terrain.md#terrainupdate) sample is emitted with the initial values of the terrain component.

## Update

### Hooks

This recorder module doesn't hook into any methods to detect changes in the component properties yet. If you need to record dynamic changes, feel free to [contribute](../../../contributing.md).

!!! info
    See the [associated proto files](../../file-format/proto-files/unity/terrain.md) for more information on the data format.