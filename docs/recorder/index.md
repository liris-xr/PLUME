---
title: Recorder
---
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
</style>
# PLUME Recorder
<p align="center">
    <img src="../images/plume_recorder_light.png" alt="plume recorder logo" width="300"/>
</p>

<br/>

The PLUME Recorder is a Unity package to record data at runtime (both in editor or built applications) without any modifications to the original project files required.
Out of the box, the recorder will record as much data as possible (see the `Recorded Data` section of the documentation) while maintaining high performances. This includes most of the data used by researchers working with virtual environments, namely:

- Object and player position/rotation
- Object appearance (material, mesh)
- Controller inputs (compatible with any [Unity Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest/) mapping)
- Eye-gaze (compatible with any [OpenXR compatible device](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.0/manual/features/eyegazeinteraction.html))
- Physiological signals (compatible with the [LabStreamingLayer](https://labstreaminglayer.org/#/))
- ...

A more exhaustive list of recorded data can be found in the `Recorded Data` section of the documentation.

Generated data can be replayed and analyzed in-situ using the [PLUME Viewer](../viewer/index.md) and analyzed ex-situ using [PLUME Python](../python/index.md).
