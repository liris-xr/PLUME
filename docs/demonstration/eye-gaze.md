# Analyze eye-gaze data
If you use a headset that integrates eye-tracking data (e.g., HTC Vive Pro Eye, Meta Quest Pro) to run the Easter Egg Hunt application, PLUME-Recorder will automatically record the position and orientation of gaze. You can use PLUME-Viewer to compute a projection of eye-gaze on the 3D scene.

## Record eye-gaze data
PLUME-Recorder records [Unity Input Actions](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/Actions.html) which loosely correspond to input from the user. Eye-gaze data are recorded through Input Actions, if you have defined actions that use the [eye-gaze pose data bindings](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.10/manual/features/eyegazeinteraction.html). These actions are part of the XRI Default Action Map provided by the XR Interaction Toolkit samples.

<p align="center">
    <img src="/demonstration/images/input_action_manager.png" alt="input action manager" width="800"/>
</p>

## Compute eye-gaze heatmap in-situ
Using PLUME-Viewer Eye-gaze Heatmap module, you can highlight objects that have been looked at. You can find the analysis module on the right side of the viewer.

* XR Camera: copy and paste the GUID of the Main Camera object. For example the Main Camera path is `XR Interaction Setup / XR Origin (XR Rig) / Camera Offset / Main Camera`.
* Projection Receiver: copy and paste the GUID of one or more object for the heatmap to be projected on. For example to project eye-gaze inside the livingroom, copy and paste the GUID of every object under the `Livingroom` object.
* Include children: if enabled, the projection will include the inserted GUID and their children in the hierarchy. For example to project eye-gaze inside the livingroom, copy and paste the GUID the `Livingroom` object __only__ and enable `Include children`.
* Coordinate System: Tracking Space or Head Space. OpenXR doesn't push a standard for the coordinate system used by HMDs eye-tracker. Depending on your headset, recorded eye-gaze will have a different coordinate system. For example when using a Meta Quest Pro, data is recorded in Tracking Space.
* Time Range: section of the record you want the heatmap to be computed on. Leave as is to take the entire record into account.

<p align="center">
    <img src="/demonstration/images/eye_gaze_heatmap.png" alt="PLUME-Viewer interaction module" width="600"/>
</p>

Click on `Generate` to create the interaction eye-gaze heatmap with selected parameters. Once computed, objects that have been gazed at directly will be highlighted. Dark blue means no gaze, Dark Red means most time spent gazing at this zone.

<p align="center">
    <img src="/demonstration/images/eye_gaze_heatmap_result.png" alt="PLUME-Viewer interaction heatmap result" width="800"/>
</p>

Generated heatmaps can be hidden from view (using eye icon) or deleted (using trash icon).

## Export generated eye-gaze heatmap for ex-situ analysis
Generated heatmaps can be exported (using download icon). Every object included in the heatmap will be exported as a point cloud. The point cloud integrates a scalar values corresponding to the time spent gazing at the object. You can use [Cloud Compare](https://www.danielgm.net/cc/) to view exported heatmaps.

TODO: add a screenshot of CloudCompare.