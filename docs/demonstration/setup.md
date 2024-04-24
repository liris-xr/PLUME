# Record your experiment with PLUME Recorder
PLUME helps you collect the data you need to make the most of experiments that use a virtual environment built with Unity.

## Install PLUME Recorder in your Unity project
!!! information
    PLUME Recorder is compatible with **Unity 2022 or later**.

1. Open the Package Manager window from `Window > Package Manager`.
2. Click on the `+` button at the top left of the Package Manager window.
3. Select `Add package from git URL...`.
4. Paste the Git URL into the text field: `https://github.com/liris-xr/PLUME-Recorder.git`
5. Click on the `Add` button.
6. Unity will now download and import the package into your project.

<p align="center">
    <img src="../images/package_manager.png" alt="package manager" width="800"/>
</p>

!!! success
    The recorder is now installed and ready to record.

## Configure the recorder to fit your needs
### Default Settings

!!! Information
    Throughout this walkthrough, we will use the default settings.

=== "Auto-Start"

    Recording automatically starts when the application is launched.

=== "Audio"

    Audio Recorder is **disabled**, audio won't be recorded.

=== "Update Rate"

    Update rate is set to 140 frames per second. It specifies the **maximum** number of frame per second recorded, but PLUME will record at application rate if under.

=== "Transform Recording Thresholds"

    Thresholds to trigger record of Transform changes is 0.001 for position and scale and 0.001 for rotation.

=== "Lab Streaming Layer"

    Lab Streaming Layer streams can be picked up for recording.

### Settings Panel
If you want to configure PLUME Recorder, the settings panel is located inside the `Project Settings` window which is accessible directly from `PLUME > Settings`.

To get more details on settings go to the PLUME-Recorder [global settings page](../recorder/global-settings.md).

<p align="center">
    <img src="../images/settings.png" alt="plume settings panel" width="800"/>
</p>

## Let's create our first record !
Press the `Play` button to start egg hunting !

If installation has been successful, PLUME will display the information messages in the console.

<p align="center">
    <img src="../images/recorder_started.png" alt="plume logs" width="800"/>
</p>

Record files are saved in the <a href="https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html">application persistent data path</a>, the path is different depending on your operating system.

=== "Windows"

    `%userprofile%\\AppData\\LocalLow\\*companyname*\\*productname*`

=== "iOS"

    `/var/mobile/Containers/Data/Application/*guid*/Documents`

=== "Android"

    `/storage/emulated/*userid*/Android/data/*packagename*`

## Issues with this step of the walkthrough ?

If you encounter any errors or issues, please <a href="https://github.com/liris-xr/PLUME-Recorder/issues">create an issue</a> or [contact us](../contact.md).
