# Analyze objects movements
User behavior is in part refleted by their movements. PLUME-Recorder is used to record the position of every object. PLUME-Viewer replays movement in 3D and displays trajectories. PLUME-Python is used to manipulate trajectory data.

## Record objects movements
PLUME-Recorder records every Transform in the scene, meaning that any movement is recorded. See the [dedicated page](../recorder/recorded-data/frame-based-data/transform.md) for more information.

## Replay objects movements and trajectories
When playing a record with PLUME-Viewer, every object that moved during the recording moves in the replay.

To compute trajectories of moving objects, use the Trajectory analysis module. You can find the analysis module on the right side of the viewer.

* Object ID: GUID of the Object you want to compute the trajectory for.
* Markers: if you have recorded Markers, they can be displayed above the trajectory.
* Teleportation tolerance: maximal distance in meter between 2 points before it is considered a teleportation.
* Teleportation segments: if enabled, teleportation will be displayed as dotted lines.
* Decimation Tolerance:
* Include rotations: if enabled, rotation gizmo will be displayed above the trajectory.

<p align="center">
    <img src="/demonstration/images/hmd_trajectory.png" alt="trajectory module within PLUME-Viewer" width="400"/>
</p>