# Get started

PLUME can be installed and used on various Unity projects (2D, 3D, XR) and platforms (Windows, Android, iOS). The installation process is different depending on the module you want to use, the instructions are detailed below.

!!! tip
    Once installed, we recommend you to check the [Beginner Tutorial](tutorials/beginner/basics/introduction.md) to get started with the toolbox.

## Installing PLUME Recorder

!!! note
    PLUME Recorder requires Unity 2022 or later.

1. Go to `Window` > `Package Manager` > `Add package from git URL...`
2. Enter the Git URL and install: 
   ```{.copy}
   https://github.com/liris-xr/PLUME-Recorder.git
   ```
3. Force recompilation with hooks from `PLUME > Force Recompile With Hooks`

## Installing PLUME Viewer

!!! note
    PLUME Viewer is available for Windows only.

1. Go to the GitHub release page [here](https://github.com/liris-xr/PLUME-Viewer/releases/latest) to download the latest version of the viewer.
2. Extract the archive in the folder of your choice.
3. Run `PLUME-Viewer.exe`

!!! tip
    You can associate `.plm` files with the viewer by right-clicking on a `.plm` file, selecting `Open with`, and choosing the viewer executable. This will allow you to open `.plm` files by double-clicking on them.

## Installing PLUME Python

!!! note
    PLUME Python requires Python 3.10 or later.

In your Python environment, run the following command:

```bash
pip install plume-python
```