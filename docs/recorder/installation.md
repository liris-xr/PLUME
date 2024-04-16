# Installation

## Prerequisites
* Unity 2022 or later

## From the Unity Package Manager
1. Open the Package Manager window from `Window > Package Manager`.
2. Click on the `+` button at the top left of the Package Manager window.
3. Select `Add package from git URL...`.
4. Paste the Git URL into the text field: `https://github.com/liris-xr/PLUME-Recorder.git`
5. Click on the `Add` button.
6. Unity will now download and import the package into your project.
7. Force recompilation with hooks from `PLUME > Force Recompile With Hooks`

!!! success
    The recorder is now installed and ready to record.

<!-- ## Manual installation
1. Download PLUME-Recorder <a href="https://github.com/liris-xr/PLUME-Recorder/releases">latest release </a>.
2. Import the downloaded package in your `Assets` folder. -->

## From Git
1. Clone the repository inside the `Packages` folder of your Unity project using the following command:
```bash
git clone --recurse-submodules https://github.com/liris-xr/PLUME-Recorder.git
```
2. Unity will import the package into your project.
3. You can now edit the source code to adapt it to your needs. Feel free to [contribute](../contributing.md).