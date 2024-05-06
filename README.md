<div align="center">
    <a href="https://github.com/liris-xr/PLUME">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="docs/images/plume_logo_dark.png">
            <source media="(prefers-color-scheme: light)" srcset="docs/images/plume_logo_light.png">
            <img alt="PLUME banner." src="docs/images/plume_logo_light.png" style="max-height: 150px">
        </picture>
    </a>
    <p>
        <a href="https://opensource.org/license/gpl-3-0"><img alt="License badge" src="https://img.shields.io/badge/license-GPLv3-blue.svg"/></a>
        <a href="https://github.com/liris-xr/PLUME/actions/workflows/docs.yml"><img alt="Documentation badge" src="https://github.com/liris-xr/PLUME/actions/workflows/docs.yml/badge.svg"/></a>
        <a href="https://discord.gg/c3evqEWMge"><img alt="Discord badge" src="https://img.shields.io/discord/1151165491767935107?logo=discord&logoColor=white&label=discord"/></a>
    </p>
</div>
<p align="center">
    Charles Javerliat, Sophie Villenave, Pierre Raimbaud, Guillaume Lavoué
    <br />
    <em>IEEE Conference on Virtual Reality and 3D User Interfaces (Journal Track)</em>
    <br />
    <a href="https://www.youtube.com/watch?v=_6krSw7fNqg"><strong>Video »</strong></a>&emsp;
    <a href="https://hal.science/hal-04488824"><strong>Paper »</strong></a>&emsp;
    <a href="https://liris-xr.github.io/PLUME/"><strong>Explore the docs »</strong></a>
    <br />
</p>

PLUME is a software toolbox that allows for the exhaustive record of XR behavioral data (including synchronous physiological signals), their offline interactive replay and analysis. PLUME is composed of three main tools:

- [PLUME Recorder](https://www.github.com/liris-xr/PLUME-Recorder) for recording data from any Unity applications.
- [PLUME Viewer](https://www.github.com/liris-xr/PLUME-Recorder) for replaying records and in-situ analysis.
- [PLUME Python](https://www.github.com/liris-xr/PLUME-Recorder) for ex-situ analysis.

We believe that PLUME can greatly benefit the scientific community by making the use of behavioral and physiological data available to as many people as possible, contributing to the reproducibility and replicability of user studies using virtual environments (XR, game design, etc), enabling the creation of large datasets, and contributing to a deeper understanding of user experience.

https://github.com/liris-xr/PLUME/assets/20073809/33369f47-a308-4bfa-8b99-edaf5a9633d0

## Getting Started

The installation of PLUME is straightforward and can be done in a few minutes at any development stage of your project. Please refer to the [getting started guide](https://liris-xr.github.io/PLUME/get-started/) to start using PLUME in your project.


## Documentation

The full documentation is available at [liris-xr.github.io/PLUME/](https://liris-xr.github.io/PLUME/). It includes a detailed description of the installation process, the file format specifications, the usage of the different tools, etc.

[![Button Docs]][Explore the docs]

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. You can [open an issue](https://github.com/liris-xr/PLUME/issues) to report a bug, request a feature, or submit a pull request.

## Contact

Discord server **(Recommended)** <a href="https://discord.gg/c3evqEWMge">
            <img alt="Discord badge" src="https://img.shields.io/discord/1151165491767935107?logo=discord&logoColor=white&label=discord"/>
        </a>

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

[Button Docs]: https://img.shields.io/badge/Explore%20the%20docs-%E2%86%92-brightgreen
[Explore the docs]: https://liris-xr.github.io/PLUME/
