# Game Object

Game Objects represent entities in the game world.

The `GameObjectRecorderModule` automatically picks up every game object in the scene and records:

- Whether the game object is active or not.
- Tag
- Name
- Layer

## Creation and destruction

The creation and destruction of a game object are recorded as a [GameObjectCreate](../../advanced/format-specifications/unity/game_object.md#gameobjectcreate) and [GameObjectDestroy](../../advanced/format-specifications/unity/game_object.md#gameobjectdestroy) sample respectively.

When created, a [GameObjectUpdate](../../advanced/format-specifications/unity/game_object.md#gameobjectupdate) sample is emitted with the initial active state, tag, name, and layer.

## Update

### Hooks

A [GameObjectUpdate](../../advanced/format-specifications/unity/game_object.md#gameobjectupdate) sample is emitted when a change in the game object properties is detected. The following methods are hooked to detect those changes:

- [Object.name](https://docs.unity3d.com/ScriptReference/Object-name.html)
- [GameObject.tag](https://docs.unity3d.com/ScriptReference/GameObject-tag.html)
- [void GameObject.SetActive(bool value)](https://docs.unity3d.com/ScriptReference/GameObject.SetActive.html)

!!! info
    See the [associated proto files](../../advanced/format-specifications/unity/game_object.md) for more information on the data format.
