# Replay a record

Replaying and inspecting records can be done with the PLUME Viewer. This standalone application is independent and completely decoupled from the initial Unity project used during recording. In practice, this means that anyone can replay a record of your experiment without having to send them your full Unity project.

<figure>
    <video width="700" controls autoplay loop>
        <source src="../assets/replay_lq.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <figcaption>Example video of a record replay in PLUME Viewer from the <a href="https://github.com/liris-xr/PLUME-Demo">Easter Egg Hunt demo</a>.</figcaption>
</figure>

## Installing the PLUME Viewer

1. Go to the GitHub release page [here](https://github.com/liris-xr/PLUME-Viewer/releases/latest) to download the latest version of the viewer.
2. Extract the archive in the folder of your choice.
3. Run `PLUME-Viewer.exe`

!!! note
    PLUME Viewer is available for Windows only.

## Building the asset bundle of your application

To replay a recording, you need to build an asset bundle of your application. The asset bundle include prefabs, textures, materials, meshes, etc. that are used in the application. This operation is required only once as assets are common to all application runs and prevents embeddings the assets in every record file.

To export the asset bundle, open your Unity project and generate it by clicking `PLUME > Build Asset Bundle`. The generated asset bundle is saved as `Assets/AssetBundles/plume_bundle.zip` in your project folder.

!!! info
    The asset bundle only includes the assets from the scenes specified in the build settings. If no scene is selected, the currently opened scene will be used.


## Opening a record

To open a record for replay, launch the viewer and select the record file to inspect. Then, you will be asked to select the asset bundle `plume_bundle.zip` generated in the previous step. The viewer will load the record and the associated assets.

When the record is loaded, you can start/pause the recording, navigate through the timeline, and inspect the data. A major benefit of this viewer is the contextualisation of temporal data such as event markers or physiological signals within the spatial environment and the associated analysis modules that will be covered in the [in-situ analysis](analysis/in-situ/index.md) section.

!!! tip
    You can associate `.plm` files with the viewer by right-clicking on a `.plm` file, selecting `Open with`, and choosing the viewer executable. This will allow you to open `.plm` files by double-clicking on them. If your asset bundle is located next to the record file, the viewer will automatically detect it and load it. This, in combination with the file association, allows you to open a record quickly by simply double-clicking on it.