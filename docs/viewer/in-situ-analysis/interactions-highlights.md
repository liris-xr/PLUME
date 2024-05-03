# Interactions Highlights

With the interactions module, you can highlight objects that have been interacted with. See more details on how PLUME-Recorder logs interactions in the [inputs section](../../recorder/recorded-data/inputs.md).

<p align="center">
    <img src="../../images/interaction_heatmap_result.png" alt="PLUME-Viewer interaction heatmap result" width="800"/>
</p>

The interactions highlights analysis module contains the following parameters:

* Interactor(s): GUID of one or more interactor.
* Interactable(s) **(Optional)**: GUID of one or more interactable. If empty, every interactable in the scene will be taken into account.
* Interaction type: Interactions as defined by the [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/interactable-events.html).  Taking the example of a Direct (or near) Interactor, `Hover` corresponds to touching an interactable, `Select` corresponds to grabbing an interactable, `Activate` is a contextual interaction executed with a selected interactable.
* Time Range: section of the record you want the heatmap to be computed on. Leave as is to take the entire record into account.

<p align="center">
    <img src="../../images/interaction_heatmap.png" alt="PLUME-Viewer interaction module" width="600"/>
</p>

Click on `Generate` to create the interaction heatmap with selected parameters. Once computed, objects that have been interacted with are highlighted in shades of red. White means no interaction, Dark Red means most number of interactions.

Generated heatmaps can be hidden from view (using eye icon) or deleted (using trash icon).