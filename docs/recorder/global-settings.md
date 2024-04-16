# Global Settings

The recorder settings are located at `Edit > Project Settings > PLUME Recorder`. You can also access it directly from `PLUME > Settings`.

| Setting | Type | Description |
|---|---|---|
| Start On Play | bool | When enabled, the recorder will begin recording as soon as the application starts. If you want to control when to start the recording you can disable this setting and call `PlumeRecorder.StartRecording("RecordName");` from any of your scripts. |
| Default Record Prefix | string | Default name for the record. The record file names are structured as follows `<record_prefix>_dd-mm-yyyy_hh-mm-ss.plm`. |
| Default Record Extra Metadata | string | Defines a string integrated within the record file. This can be used to record additional contextual data such as: experiment condition, location, etc. |

!!! warning
    While it might be tempting to add all of the additional contextual data in the extra metadata field, we strongly recommended the creation of new `.proto` file and to [contribute](../contributing.md) to the project so that other people can benefit from this specification. By integrating new `.proto` specifications for metadata, you will also contribute to data standardization across projects.