# Eye-gaze heatmap (Experimental 🧪)

!!! warning "Experimental feature"
    The eye-gaze heatmap is an experimental feature. It is still under development and may present some artifacts.


With the eye-gaze module, you can create heatmaps that show where the user looked at the most. In pratice, the direction of gaze is projected from the position of the eyes in a cone-shaped perspective towards the objects in the scene. The heatmap is bound to the objects, it takes into account occlusions and the dynamic nature of the scene.

<figure>
    <video width="600" controls autoplay loop>
        <source src="../../../../assets/in-situ-analysis/eye_gaze_heatmap_generation.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <figcaption>Presentation of the eye-gaze algorithm integrated in the viewer.</figcaption>
</figure>

The eye-gaze heatmap analysis module contains the following parameters:

![Eye-gaze heatmap module](../../../assets/in-situ-analysis/eye_gaze_heatmap_module.png){ width="400", align="left" }

* XR Camera: GUID of the Main Camera object.
* Projection Receiver: GUID of one or more object for the heatmap to be projected on.
* Include children: if enabled, the projection will include the GUID inserted in 'Projection Receiver' and their children in the hierarchy.
* Coordinate System: Tracking Space or Head Space. OpenXR doesn't push a standard for the coordinate system used by HMDs eye-tracker. Depending on your headset, recorded eye-gaze will have a different coordinate system (eg. Meta Quest Pro uses `Tracking Space`; HTC Vive Pro Eye uses `Head Space`).
* Time Range: section of the record you want the heatmap to be computed on. Leave as is to take the entire record into account.

<br>
Click on `Generate` to create the interaction eye-gaze heatmap with selected parameters. Generated heatmaps can be hidden from view (using eye icon) or deleted (using trash icon).

![Eye-gaze heatmap result](../../../assets/in-situ-analysis/eye_gaze_heatmap_result.png){ width="600" }
/// caption
Result of the eye-gaze heatmap visualization. The duration of the gaze is represented by the color intensity from blue (no time spent) to red (most time spent).
///