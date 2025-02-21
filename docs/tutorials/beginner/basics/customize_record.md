# Recording event markers

When recording an experiment, you might want to add information to your records to fulfill your specific research needs. In this section, we will show you how to add simple event markers to your records.

!!! info
    If you are interested in recording more advanced custom data, please refer to the [recording custom data](./custom_data.md) tutorial.

Markers consists of a labelled timestamp that can be used to indicate specific events in your application. Recording an event marker can be done with a single line of code. In the following example, we will add a marker when the user picks up an egg during the Easter Egg Hunt by slightly modifying one of the existing scripts.

1. In Unity, navigate in the project's file, open the `Scripts` folder and open `EasterEgg.cs` with a C# IDE (e.g., [Visual Studio](https://visualstudio.microsoft.com/fr/vs/community/), [JetBrains Rider](https://www.jetbrains.com/fr-fr/rider/)).
```C# title="EasterEgg.cs"
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

[RequireComponent(typeof(UnityEngine.XR.Interaction.Toolkit.Interactables.XRSimpleInteractable))]
public class EasterEgg : MonoBehaviour
{
    public Quest quest;

    private UnityEngine.XR.Interaction.Toolkit.Interactables.XRSimpleInteractable _interactable;

    private void Start()
    {
        _interactable = GetComponent<UnityEngine.XR.Interaction.Toolkit.Interactables.XRSimpleInteractable>();
        _interactable.hoverEntered.AddListener(ObjectPickedUp);
    }

    private void ObjectPickedUp(HoverEnterEventArgs args)
    {
        quest.OnEggPickUp(this);
    }
}
```
2. To use PLUME Recorder in your script, you need to import the associated namespace at the beginning of the file.
```C#
using PLUME.Core.Recorder;
```
3. We want to log when the user picks up an egg. To do so, add the following line to the ```ObjectPickedUp``` function.
```C#
PlumeRecorder.RecordMarker("Egg Pick Up");
```
4. Now, everytime this function is called, e.g. when a user picks up an egg, a timestamped marker "Egg Pick Up" will be recorded alongside other data.
```C# title="EasterEgg.cs"
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;
using PLUME.Core.Recorder;

[RequireComponent(typeof(UnityEngine.XR.Interaction.Toolkit.Interactables.XRSimpleInteractable))]
public class EasterEgg : MonoBehaviour
{
    public Quest quest;

    private UnityEngine.XR.Interaction.Toolkit.Interactables.XRSimpleInteractable _interactable;

    private void Start()
    {
        _interactable = GetComponent<UnityEngine.XR.Interaction.Toolkit.Interactables.XRSimpleInteractable>();
        _interactable.hoverEntered.AddListener(ObjectPickedUp);
    }

    private void ObjectPickedUp(HoverEnterEventArgs args)
    {
        quest.OnEggPickUp(this);
        PlumeRecorder.RecordMarker("Egg Pick Up");
    }
}
```

!!! note
    If your C# IDE does not recognize Unity classes and functions, thus not displaying autocompletion and compiling errors, ensure the Unity Editor uses your chosen IDE to open `.cs` files. In Unity click on `Edit -> Preferences`. Under External Tools, select your IDE. Unity installs Visual Studio Community by default.