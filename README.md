<a name="readme-top"></a>
<div align="center">
    <a href="https://github.com/liris-xr/PLUME">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="/Documentation~/Images/plume_banner_dark.png">
            <source media="(prefers-color-scheme: light)" srcset="/Documentation~/Images/plume_banner_light.png">
            <img alt="PLUME banner." src="/Documentation~/Images/plume_banner_light.png">
        </picture>
    </a>
    <br />
    <br />
    <p align="center">
        <strong>PLUME: Record, Replay, Analyze and Share User Behavior in 6DoF XR Experiences</strong>
        <br />
        Charles Javerliat, Sophie Villenave, Pierre Raimbaud, Guillaume Lavoué
        <br />
        <em>(Journal Track) IEEE Conference on Virtual Reality and 3D User Interfaces</em>
        <br />
        <a href="https://www.youtube.com/watch?v=_6krSw7fNqg"><strong>Video »</strong><a>
        <a href="https://hal.science/hal-04488824"><strong>Paper »</strong></a>
        <a href="https://github.com/liris-xr/PLUME/wiki/"><strong>Explore the docs »</strong></a>
        <br />
        <br />
        <a href="https://github.com/liris-xr/PLUME/issues">Report Bug</a>
        ·
        <a href="https://github.com/liris-xr/PLUME/issues">Request Feature</a>
    </p>
</div>

<img alt="PLUME viewer." src="/Documentation~/Images/plume_viewer_teaser.png">

<details>
    <summary>Table of Contents</summary>
    <ol>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#roadmap">Roadmap</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#citation">Citation</a></li>
    </ol>
</details>

## Getting Started

In order to record your virtual experiment, you will need to install the <a href="https://www.github.com/liris-xr/PLUME-Recorder">PLUME-Recorder</a> in your Unity project. The installation instructions are available <a href="https://github.com/liris-xr/PLUME-Recorder?tab=readme-ov-file#getting-started">here</a>.

When you are done recording your experiment, you can view and analyze your record files using the <a href="https://www.github.com/liris-xr/PLUME-Viewer">PLUME-Viewer</a> standalone application. The installation instructions are available <a href="https://github.com/liris-xr/PLUME-Viewer?tab=readme-ov-file#getting-started">here</a>.

If you need to analyze your record with other tools and languages (R, Python, etc), you can extract the data from the record files and export it to dataframes, CSV, XDF, and other formats using <a href="https://www.github.com/liris-xr/PLUME-Python">PLUME-Python</a>. The installation instructions are available <a href="https://github.com/liris-xr/PLUME-Python?tab=readme-ov-file#getting-started">here</a>.

## About

From education to medicine to entertainment, a wide range of industrial and academic fields now utilize eXtended Reality (XR) technologies.

This diversity and growing use are boosting research and leading to an increasing number of XR experiments involving human subjects. The main aim of these studies is to understand the user experience in the broadest sense, such as the user cognitive and emotional states.

Behavioral data collected during XR experiments, such as user movements, gaze, actions, and physiological signals constitute precious assets for analyzing and understanding the user experience. While they contribute to overcome the intrinsic flaws of explicit data such as post-experiment questionnaires, the required acquisition and analysis tools are costly and challenging to develop, especially for 6DoF (Degrees of Freedom) XR experiments. Moreover, there is no common format for XR behavioral data, which restrains data-sharing, and thus hinders wide usages across the community, replicability of studies, and the constitution of large datasets or meta-analysis.

In this context, we present PLUME, an open-source software toolbox (<a href="https://www.github.com/liris-xr/PLUME-Recorder">PLUME Recorder</a>, <a href="https://www.github.com/liris-xr/PLUME-Viewer">PLUME Viewer</a>, <a href="https://www.github.com/liris-xr/PLUME-Python">PLUME Python</a>) that allows for the exhaustive record of XR behavioral data (including synchronous physiological signals), their offline interactive replay and analysis (with a standalone application), and their easy sharing due to our compact and interoperable data format.
We believe that PLUME can greatly benefit the scientific community by making the use of behavioral and physiological data available for the greatest, contributing to the reproducibility and replicability of XR user studies, enabling the creation of large datasets, and contributing to a deeper understanding of user experience.

[![PLUME demo video](/Documentation~/Images/video_thumbnail.png)](https://www.youtube.com/watch?v=_6krSw7fNqg)

</br>
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="/Documentation~/Images/plume_recorder_header_dark.png">
    <source media="(prefers-color-scheme: light)" srcset="/Documentation~/Images/plume_recorder_header_light.png">
    <img alt="PLUME-Recorder header." src="/Documentation~/Images/plume_recorder_header_light.png">
</picture>
</br>

The <a href="https://www.github.com/liris-xr/PLUME-Recorder">PLUME Recorder</a> is the cornerstone of the toolbox. It allows for continuously recording the state of the virtual environment in a Unity application with minimal impact on performances. By default, the recorder will record as much data as possible, namely object position, appearance, sound, interactions, and physiological signals (through a <a href="https://labstreaminglayer.org/">LabStreamingLayer</a> integration). The recorder also allows for custom data recording, such as event markers or custom-defined data structures in <a href="https://protobuf.dev/overview/">Google Protocol Buffer</a> files. This format is the one we use for all of our samples as it allows for a fast and frugal serialization, is platform-neutral and can be de-serialized in any language. The PLUME Recorder is compatible with Windows, Android, and iOS and with standalone devices. For the VR use case, we use the functionalities of OpenXR as much as possible so that it is compatible with many headsets. As the record files all follow the same serialization process and data format, they can be used interoperably across devices. For example, one could record an experiment on a standalone Android device and analyze the record file on a Windows machine, without the need for the original Unity project.

</br>
<div align="center">
<a href="https://github.com/liris-xr/PLUME-Viewer">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="/Documentation~/Images/plume_viewer_dark.png">
    <source media="(prefers-color-scheme: light)" srcset="/Documentation~/Images/plume_viewer_light.png">
    <img alt="PLUME viewer logo." src="/Documentation~/Images/plume_viewer_light.png" height="80">
</picture>
</a>
</div>
</br>

The <a href="https://www.github.com/liris-xr/PLUME-Viewer">PLUME Viewer</a> is a standalone application for viewing and analyzing the record files independently of the Unity project. It offers analysis modules such as interactions analysis, 3D trajectories, in-context physiological signals tracks, position and eye gaze heatmaps for which export is available as point clouds with the scalar field embedded. PLUME Viewer is useful to observe a recorded experiment like a video in a media player, as it does not require anything more than the record files to reconstruct the VE.

</br>
<div align="center">
<a href="https://github.com/liris-xr/PLUME-Python">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="/Documentation~/Images/plume_python_dark.png">
    <source media="(prefers-color-scheme: light)" srcset="/Documentation~/Images/plume_python_light.png">
    <img alt="PLUME python logo." src="/Documentation~/Images/plume_python_light.png" height="80">
</picture>
</a>
</div>
</br>

The interoperability of the record files allows for other language to load those files for external analysis. <a href="https://www.github.com/liris-xr/PLUME-Python">PLUME Python</a> is a module that can load record files using the Protobuf package to filter and convert the data into more commonly used formats in data analysis like pandas dataframe or CSV files. Embedded data such as LabStreamingLayer's samples can be exported to XDF files for external use in tools such as <a href="https://github.com/cbrnr/sigviewer">SigViewer</a>, <a href="https://eeglab.org/">EEGLAB</a> or <a href="https://github.com/sccn/mobilab">MoBILAB</a>.

## Roadmap

See the [open issues](https://github.com/liris-xr/PLUME/issues) for a full list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
Don't forget to give the project a star! Thanks again!

## License

Distributed under the <a rel="license" href="https://github.com/liris-xr/PLUME/blob/master/LICENSE">GPLv3 License</a>.

## Contact

</br>
<div align="center">
<a href="https://discord.gg/c3evqEWMge">
<picture>
    <img alt="PLUME discord server" src="/Documentation~/Images/discord.png" height="80">
</picture>
</a>
</div>
</br>

Charles JAVERLIAT - charles.javerliat@gmail.com

Sophie VILLENAVE - sophie.villenave@ec-lyon.fr

## Citation
```
@article{javerliat_plume_2024,
	title = {{PLUME}: {Record}, {Replay}, {Analyze} and {Share} {User} {Behavior} in {6DoF} {XR} {Experiences}},
	url = {https://ieeexplore.ieee.org/document/10458415},
	doi = {10.1109/TVCG.2024.3372107},
	journal = {IEEE Transactions on Visualization and Computer Graphics},
	author = {Javerliat, Charles and Villenave, Sophie and Raimbaud, Pierre and Lavoué, Guillaume},
	year = {2024},
	note = {Conference Name: IEEE Transactions on Visualization and Computer Graphics},
	pages = {1--11}
}
```