# Hooks injection

## Principle

For performance reasons and to prevent users from having to modify their project to record data, we use _Intermediate Language Code Weaving_ to replace calls to the Unity Engine by calls to an internal hook method. The hook performs the same operation, but also records the associated with the call.

??? example "Example of a hook injection"
    Suppose you created a script that creates a new GameObject like so:
    ```cs
    var gameObject = new GameObject( "Awesome Object");
    ```
    This is what the original IL code for this operation would look like:
    ```cs
    ldstr "Awesome Object"
    newobj instance void UnityEngine.GameObject::.ctor(string)
    ```
    After Unity finished generating the IL code, we scan the generated assemblies for the GameObject constructor call, and replace it with a call to a custom hook called `GameObjectHooks.CreateAndNotify`. The modified IL code will now look like this:
    ```cs
    ldstr "Awesome Object"
    call class UnityEngine.GameObject PLUME.Base.Hooks.GameObjectHooks::CreateAndNotify(string)
    ```
    Internally, `CreateAndNotify` calls the original constructor, but also fires an event that recorder modules can subscribe to in order to record the data:
    ```cs
    public static GameObject CreateAndNotify(string name)
    {
        // Call to the original constructor.
        var go = new GameObject(name);
        // Fire an event to record the creation of the game object.
        OnCreated(go);
        // Returns the newly created game object, as the constructor call would.
        return go;
    }
    ```

This method presents several benefits:

- Low impact on performances compared to polling for changes.
- Requires no modification of the project scripts.
- Drastically reduces the time spent to install the recorder compared to other tools.
- Can be uninstalled without breaking the project.

Hooks are automatically injected at compile time in the assemblies listed in the [settings](#settings). If automatic injection wasn't triggered, injection can be forced with `PLUME > Force Recompile With Hooks`.

## Settings

The settings for hooks injection are located at `Edit > Project Settings > PLUME Recorder > Hooks`.

| Setting | Type | Description |
|---|---|---|
| Injected Assemblies | string[] | Lists of assemblies (`.dll` files) in which hooks will be injected after being compiled to Intermediate Language. |