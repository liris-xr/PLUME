# Physiological signals

The PLUME Recorder offers the capability to synchronously record physiological signals with the virtual environment itself (eye tracking, heart rate, electrocardiogram, electroencephalogram etc.). In order to support a wide variety of devices, the recorder integrates a receiver for applications that uses the [Lab Streaming Layer (LSL)](https://labstreaminglayer.org/#/).

!!! quote
    LSL is an open-source networked middleware ecosystem to stream, receive, synchronize, and record neural, physiological, and behavioral data streams acquired from diverse sensor hardware.
    
LSL has an already well-developed community and, as stated in their documentation, is compatible with the majority of EEG systems on the market and other biosignal hardware (see the [list of supported devices and tools](https://labstreaminglayer.readthedocs.io/info/supported_devices.html)). By making PLUME able to record LSL streams, this further reduces the development time needed for researchers that seek to integrate synchronized physiological data in their recordings.