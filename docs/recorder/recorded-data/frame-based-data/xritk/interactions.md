# Interactions

The `XRBaseInteractableRecorderModule` and `XRBaseInteractorRecorderModule` records XR Interaction Toolkit [interactable events](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/interactable-events.html) and [interactor events](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/interactor-events.html?q=interactor) respectively.

These recording modules automatically picks up every Interactable and Interactor in the scene and records the associated events.

## Update

### Hooks

The `XRBaseInteractableRecorderModule` hooks into the following methods to detect interactable events:

- [IXRHoverInteractable.hoverEntered](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactables.IXRHoverInteractable.html#UnityEngine_XR_Interaction_Toolkit_Interactables_IXRHoverInteractable_hoverEntered)
- [IXRHoverInteractable.hoverExited](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactables.IXRHoverInteractable.html#UnityEngine_XR_Interaction_Toolkit_Interactables_IXRHoverInteractable_hoverExited)
- [IXRSelectInteractable.selectEntered](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactables.IXRSelectInteractable.html#UnityEngine_XR_Interaction_Toolkit_Interactables_IXRSelectInteractable_selectEntered)
- [IXRSelectInteractable.selectExited](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactables.IXRSelectInteractable.html#UnityEngine_XR_Interaction_Toolkit_Interactables_IXRSelectInteractable_selectExited)
- [IXRActivateInteractable.activated](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactables.IXRActivateInteractable.html#UnityEngine_XR_Interaction_Toolkit_Interactables_IXRActivateInteractable_activated)
- [IXRDeactivateInteractable.deactivated](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactables.IXRActivateInteractable.html#UnityEngine_XR_Interaction_Toolkit_Interactables_IXRActivateInteractable_deactivated)

The `XRBaseInteractorRecorderModule` hooks into the following methods to detect interactable events:

- [IXRHoverInteractor.hoverEntered](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactors.IXRHoverInteractor.html#UnityEngine_XR_Interaction_Toolkit_Interactors_IXRHoverInteractor_hoverEntered)
- [IXRHoverInteractor.hoverExited](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactors.IXRHoverInteractor.html#UnityEngine_XR_Interaction_Toolkit_Interactors_IXRHoverInteractor_hoverExited)
- [IXRSelectInteractor.selectEntered](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactors.IXRSelectInteractor.html#UnityEngine_XR_Interaction_Toolkit_Interactors_IXRSelectInteractor_selectEntered)
- [IXRSelectInteractor.selectExited](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/api/UnityEngine.XR.Interaction.Toolkit.Interactors.IXRSelectInteractor.html#UnityEngine_XR_Interaction_Toolkit_Interactors_IXRSelectInteractor_selectExited)