# Recording custom data

Every experiment is unique and may require recording custom data. PLUME provides a way to record custom data in addition to the default data recorded through methods callable from any of your Unity script.

## 1. Defining the data structure

As PLUME relies on Protobuf to define the data structure, you will first need to create a `.proto` file. Proto files provide a handy way of defining the data structure in a language-neutral manner, that can be compiled to code in various languages (C#, Python, C++, etc). You can find more information about Protobuf [here](https://developers.google.com/protocol-buffers).

Let's start by defining a custom message. In our example we will create a message containing information about a person, in a file `person.proto`:

```proto
syntax = "proto3";

message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
```

## 2. Compiling the `.proto` file to C#

To be able to send the custom data with the recorder, you will need to compile the `.proto` file to C# code. You can do this using the `protoc` compiler.

### Install the Protobuf compiler

1. Download the latest version of the `protoc` compiler from the [official repository releases](https://github.com/protocolbuffers/protobuf/releases/tag/v26.1) (for Windows, this would typically be the `protoc-XX.YY-win64.zip` file).
2. Unzip the file wherever you want on your computer and add the `bin` folder to your system's PATH.
3. You can ensure that the compiler is correctly installed by running `protoc --version` in a terminal.
4. Compile the `.proto` file to C# using the following command:
    ```bash
    protoc --csharp_out=outputFolderName ./person.proto
    ```
5. The generated C# file will be located in the `outputFolderName` folder, in this case, the file will be named `Person.cs`.

## 3. Recording the custom data

You can now copy the generated C# file to your Unity project. From anywhere in your scripts, you can now create an instance of the custom message and send it to the recorder:

=== "Timestamped samples"
    ```csharp
    var person = new Person
    {
        Name = "John Doe",
        Id = 1234,
        Email = "john.doe@example.com"
    };

    PlumeRecorder.RecordTimestampedManagedSample(person);
    ```

=== "Timeless samples"
    ```csharp
    var person = new Person
    {
        Name = "John Doe",
        Id = 1234,
        Email = "john.doe@example.com"
    };

    PlumeRecorder.RecordTimelessManagedSample(person);
    ```

!!! success
    You have successfully recorded custom data with the recorder, see [how to read custom data using the Python API](../../python/advanced/reading-custom-data.md).

### 4. Compile with PLUME-Protos dependencies *(Optional)*

For some custom data, you may need to import messages from the PLUME Protos (eg. identifiers protos, vector3, color, etc), for example:

```proto
syntax = "proto3";

import "common/color.proto";
import "common/matrix4x4.proto";

message CustomData {
    plume.sample.common.Color color = 1;
    plume.sample.common.Matrix4x4 transform = 2;
}
```

To do so, you will need to install the PLUME-Protos repository and compile the `.proto` file with the dependencies.

1. Clone the PLUME-Protos repository where you want on your computer using the following command:

    === "HTTPS"
        ```bash
        git clone --recurse-submodules https://github.com/liris-xr/PLUME-Protos.git
        ```
    === "SSH"
        ```bash
        git clone --recurse-submodules git@github.com:liris-xr/PLUME-Protos.git
        ```

2. Compile the `.proto` file with the dependencies using the following command:

    ```bash
    protoc --csharp_out=outputFolderName --proto_path=./ --proto_path=path/to/PLUME-Protos/ ./custom_data.proto
    ```