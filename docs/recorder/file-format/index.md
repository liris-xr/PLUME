# File format

## Overview

The data collected by the recorder is saved in a single `.plm` file as the recording progresses. The file is written in binary and uses [Protobuf](https://protobuf.dev/) to serialize record samples in a language-neutral, platform-neutral manner, maximizing interoperability of the save file between languages and workflows.

To save space we compress the data on-the-fly using [LZ4](https://lz4.org/), a lossless dynamic compression algorithm.

!!! note
    The original paper of PLUME mentionned the use of the [Deflate algorithm](https://www.rfc-editor.org/rfc/rfc1951) through gzip. While Deflate was fast enough for most cases, we noticed some latencies in the serialization thread due to the compression speed on our stress-test benchmarks (~10000 moving objects), resulting in a long wait time at the end of recording for serialization to complete.
    
    By using LZ4, we ensured that the compression speed would not be a limit for heavy scenes, with a compression speed of up to 780 MB/s with LZ4 versus 100 MB/s for Deflate.

The file is composed a sequence of serialized [packed samples](#sample-packing), prefixed by their length.

## Sample packing

To allow for maximum extensibility, each sample payload is packed in a [Any](https://protobuf.dev/programming-guides/proto3/#any) type along with an optional timestamp in nanoseconds. Timestamp is optional so that one can record data that is not bound to a specific time, like an application setting, demographics, etc.

```proto title="packed_sample.proto"
--8<-- "external/PLUME-Protos/packed_sample.proto"
```