# Position Heatmap

With the position heatmap module, you can create heatmaps that show where objects have stayed the most. In practice, the position of the object is projected orthogonally towards the ground (-Y axis).

<figure>
    <video width="800" height="600" controls autoplay loop>
        <source src="../../videos/position_heatmap.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <figcaption>Realtime generation of the position heatmap in PLUME viewer of the user head mounted display projected on the floor of the scene.</figcaption>
</figure>

The position heatmaps analysis module contains the following parameters:

* Projection Caster: GUID of the object you want to compute the heatmap for.
* Projection Receiver: GUID of one or more object for the heatmap to be projected on.
* Include children: if enabled, the projection will include the GUID inserted in 'Projection Receiver' and their children in the hierarchy.
* Time Range: section of the record you want the heatmap to be computed on. Leave as is to take the entire record into account.

<p align="center">
    <img src="../../images/position_heatmap.png" alt="PLUME-Viewer position heatmap module" width="600"/>
</p>

Click on `Generate` to create the position heatmap with selected parameters. Once computed, position that have been most visitied highlighted. Dark blue means no time spent at this position, Dark Red means most time spent at this position.

<p align="center">
    <img src="../../images/position_heatmap_result.png" alt="PLUME-Viewer position heatmap result" width="800"/>
</p>

Generated heatmaps can be hidden from view (using eye icon) or deleted (using trash icon).