# Markers

Markers are a way to mark specific points in time during a recording. They can be used to indicate specific events, such as the start of a new task, a new trial, or any other event that needs to be labelled and referenced later during analysis.

Markers are specific to each experiment. To record a marker, from any script in your project, simply call the following method when recording is active:
```csharp
PlumeRecorder.RecordMarker("MyMarkerLabel");
```
The marker will be automatically timestamped with the current time in the recording.

!!! info
    See the [associated proto file](../file-format/proto-files/common/marker.md) for more information on the data format.