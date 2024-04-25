# Review your Easter egg hunting skills
You can replay your performance using PLUME-Viewer. If you don't have any record file, you can create one by following the [previous tutorial](setup.md) or downloading [sample files](https://github.com/liris-xr/PLUME-Demo/tree/master/EasterEggHunt/Samples).

## Build *Easter Egg Hunt* asset bundle
To replay your recordings, you need an [Asset Bundle](../recorder/asset-bundle.md), which countains the project assets in a single file.
Going back to the Unity Editor of the *Easter Egg Hunt* project, build the asset bundle by going to `PLUME > Build Asset Bundle`. An archive named `plume_bundle.zip` will be generated under `Assets/AssetBundles/`.

!!! info
    This step is only required once as it is common to every records for a given project.

## Download PLUME-Viewer
From PLUME Viewer GitHub access the <a href="https://github.com/liris-xr/PLUME-Viewer/releases">releases page</a>.

<p align="center">
    <img src="../images/github_releases.png" alt="github releases" width="800"/>
</p>

From here go the latest release page, and download `PLUME-Viewer.zip`.

<p align="center">
    <img src="../images/latest_release.png" alt="github latest release" width="800"/>
</p>

Unzip `PLUME-Viewer.zip` where you see fit on your computer.

## Let's replay our experiment !
Execute `PLUME-Viewer.exe`.

<p align="center">
    <img src="../images/file_plume_executable.png" alt="github latest release" width="800"/>
</p>

!!! tip
    You can associate the `.plm` file extension to `PLUME-Viewer.exe` to quickly open record files in the viewer.

When launching PLUME-Viewer, you are prompted to open your `.plm` file and then the associated `plume_bundle.zip` built earlier.

!!! tip
    By default, the viewer will look for the asset bundle next to the record file. By placing the `plume_bundle.zip` in the same folder as the `.plm` files, the viewer will not ask for it when opening a record.

On openning, replay will start automatically. You can navigate your record like you would a video by using the media bar. See [PLUME-Viewer documentation](../viewer.md) for more details on functionalities.

<p align="center">
    <img src="../images/media_bar.png" alt="github latest release" width="800"/>
</p>

<video align="center" width="800" height="600" controls>
  <source src="../video/free_view_replay.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

## Issues with this step of the walkthrough ?

If you encounter any errors or issues, please <a href="https://github.com/liris-xr/PLUME-Viewer/issues">create an issue</a> or [contact us](../contact.md).