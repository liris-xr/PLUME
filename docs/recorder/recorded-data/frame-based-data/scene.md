# Scene

During recording, the scene might change. These changed are recorded automatically by the `SceneRecorderModule`.

When a scene is loaded or unloaded, a [LoadScene](../../advanced/format-specifications/unity/scene.md#loadscene) or [UnloadScene](../../advanced/format-specifications/unity/scene.md#unloadscene) sample is emitted respectively. When the active scene changes, an [ChangeActiveScene](../../advanced/format-specifications/unity/scene.md#changeactivescene) sample is emitted.

## Update

### Hooks

This recorder module hooks into the following methods to detect change of scene:

- [SceneManager.sceneLoaded](https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager-sceneLoaded.html)
- [SceneManager.sceneUnloaded](https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager-sceneUnloaded.html)
- [SceneManager.activeSceneChanged](https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager-activeSceneChanged.html)

!!! info
    See the [associated proto files](../../advanced/format-specifications/unity/scene.md) for more information on the data format.