# Physiological signals

Physiological signals are used to monitor the body's response to stimuli. They can be used to measure the participant's emotional state, cognitive load, or other physiological responses. They provide a more objective measure of the participant's state than self-reporting.

The recorder offers the capability to synchronously record physiological signals (eye tracking, heart rate, electrocardiogram, electroencephalogram etc.) with the virtual environment itself. In order to support a wide variety of devices, it integrates a recorder module for data sent on the [Lab Streaming Layer (LSL)](https://labstreaminglayer.org/#/).

!!! quote
    LSL is an open-source networked middleware ecosystem to stream, receive, synchronize, and record neural, physiological, and behavioral data streams acquired from diverse sensor hardware.
    
LSL has an already well-developed community and, as stated in their documentation, is compatible with the majority of EEG systems on the market and other biosignal hardware (see the [list of supported devices and tools](https://labstreaminglayer.readthedocs.io/info/supported_devices.html)). By making PLUME able to record LSL streams, this further reduces the development time needed for researchers that seek to integrate synchronized physiological data in their recordings.

A [StreamOpen](../file-format/proto-files/lsl/lsl_stream.md#streamsample) sample is emitted every time a new stream is detected, and a [StreamClose](../file-format/proto-files/lsl/lsl_stream.md#streamclose) sample is emitted when the stream is closed. The data itself is stored in a [StreamSample](../file-format/proto-files/lsl/lsl_stream.md#streamsample) sample.

When receiving data from a LSL stream, its timestamp is corrected to take into account any network latency and to be converted into the same time reference as the rest of the recorded data [timestamps](../timestamps.md). This is made possible thanks to the [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) implemented by LSL to synchronize the clocks of the devices.

!!! info
    See the [associated proto files](../file-format/proto-files/lsl/lsl_stream.md) for more information on the data format.