# Unique identification

To link back data to the game object/component it belongs to, it is necessary to have some kind of unique identification system. Moreover, identifying objects across multiple executions is also challenging but crucial for multi-record analysis (eg. aggregated heatmaps, trajectories, etc).

The Unity engine uses a GUID system to uniquely identify objects across executions. However, this implementation is not available at runtime. As a consequence, we implemented our own GUID system to uniquely identify objects across executions, without the need for any custom component attached to the objects. The registries are automatically updated in the editor and automatically embedded in builds to access the GUIDs at runtime. New objects dynamically created at runtime will get a randomly generated GUID assigned to them.

This plugin, named Unity-Runtime-GUID, is embedded in the recorder, and is [available on GitHub](https://github.com/cjaverliat/Unity-Runtime-GUID) as well.

## GUID format

GUIDs are composed of 32 hexadecimal characters (eg. b3d33f3c841246a28380a04419a85e70).