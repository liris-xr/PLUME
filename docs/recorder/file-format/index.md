# File format

## Overview

Data collected by the recorder is saved in a single `.plm` file as the recording progresses. The file is written in binary and uses [Protobuf](https://protobuf.dev/) to serialize record samples in a language-neutral, platform-neutral manner, maximizing interoperability of the save file between languages and workflows.

To save space we compress the data on-the-fly using [LZ4](https://lz4.org/), a lossless dynamic compression algorithm.

!!! note
    The original paper of PLUME mentionned the use of the [Deflate algorithm](https://www.rfc-editor.org/rfc/rfc1951) through gzip. While Deflate was fast enough for most cases, we noticed some latencies in the serialization thread due to the compression speed on our stress-test benchmarks (~10000 moving objects), resulting in a long wait time at the end of recording for serialization to complete.
    
    By using LZ4, we ensured that the compression speed would not be a limit for heavy scenes, with a compression speed of up to 780 MB/s with LZ4 versus 100 MB/s for Deflate.

The file contains a sequence of serialized [packed samples](#sample-packing), prefixed by their length.

## Packed samples

Recorded data is specified in `.proto` files. This file format has the advantage of being easily convertible to data structures in several languages (C#, Python, C/C++, etc). In practice, this means that the specification of the recorded data is decoupled from the recorder itself, and also allows for reading the resulting `.plm` files from any language of your liking. This is what we use for [PLUME Python](../../python/index.md).

??? example "Example of a proto file"
    A proto file is defined by a list of properties with a type, a name, and an id. For more information on the `.proto` file format, see the [documentation](https://protobuf.dev/programming-guides/proto3/).

    ```proto
    message Demographics {
        Gender gender = 1;
        uint32 age = 2;
        float weight = 3;

        enum Gender {
            Unspecified = 0;
            Female = 1;
            Male = 2;
        }
    }
    ```

Each sample is packed in a `PackedSample`. The data itself is encapsulated in the payload field as an [any](https://protobuf.dev/programming-guides/proto3/#any) type. The packed samples also contain an optional [timestamp](../timestamps.md).

```proto title="packed_sample.proto"
--8<-- "external/PLUME-Protos/packed_sample.proto"
```

All of the proto files used internally by the PLUME Recorder can be found in the `Proto files` section.
