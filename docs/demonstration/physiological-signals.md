# Analyze physiological signals
PLUME integrates the [Lab Streaming Layer](https://labstreaminglayer.org/#/) ecosystem to seamlessly record physiological signals from any compatible hardware. See the [dedicated page](../recorder/recorded-data/physiological-signals.md) for more details.

## Record physiological signals
For this walkthrough, we used a [Polar H9](https://www.polar.com/fr/sensors/h9-heart-rate-sensor) heart rate sensor belt.

??? example "Python script to create an LSL Stream for the Polar H9"
    For this script to work, you need to install PyLSL, Asyncio and BitStruct packages in your Python environment.
    
    ```Python
    from pylsl import StreamInfo, StreamOutlet

    import asyncio
    import bitstruct
    import struct

    from bleak import BleakClient
    from bleak.uuids import uuid16_dict

    uuid16_dict = {v: k for k, v in uuid16_dict.items()}

    ## UUID for model number ##
    MODEL_NBR_UUID = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(uuid16_dict.get("Model Number String"))

    ## UUID for manufacturer name ##
    MANUFACTURER_NAME_UUID = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(uuid16_dict.get("Manufacturer Name String"))

    ## UUID for battery level ##
    BATTERY_LEVEL_UUID = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(uuid16_dict.get("Battery Level"))

    HR_MEAS = "00002A37-0000-1000-8000-00805F9B34FB"

    OUTLET = []

    async def run(address, debug=False):

        async with BleakClient(address) as client:
            connected = await client.is_connected()
            print("Connected: {0}".format(connected))

            model_number = await client.read_gatt_char(MODEL_NBR_UUID)
            print("Model Number: {0}".format("".join(map(chr, model_number))), flush=True)

            manufacturer_name = await client.read_gatt_char(MANUFACTURER_NAME_UUID)
            print("Manufacturer Name: {0}".format("".join(map(chr, manufacturer_name))), flush=True)

            battery_level = await client.read_gatt_char(BATTERY_LEVEL_UUID)
            print("Battery Level: {0}%".format(int(battery_level[0])), flush=True)

            def hr_val_handler(sender, data):
                """Simple notification handler for Heart Rate Measurement."""
                print("HR Measurement raw = {0}: {1}".format(sender, data))
                (hr_fmt,
                snsr_detect,
                snsr_cntct_spprtd,
                nrg_expnd,
                rr_int) = bitstruct.unpack("b1b1b1b1b1<", data)
                if hr_fmt:
                    hr_val, = struct.unpack_from("<H", data, 1)
                else:
                    hr_val, = struct.unpack_from("<B", data, 1)
                print(f"HR Value: {hr_val}")
                OUTLET.push_sample([hr_val])

            await client.start_notify(HR_MEAS, hr_val_handler)

            while await client.is_connected():
                await asyncio.sleep(1)



    def StartStream(STREAMNAME):

        info = StreamInfo(STREAMNAME, 'HR', 1, 1, 'float32', 'E6:C9:75:A1:6C:4E')

        info.desc().append_child_value("manufacturer", "Polar")
        
        return StreamOutlet(info)

    if __name__ == "__main__":
        address = ("E6:C9:75:A1:6C:4E")
        loop = asyncio.get_event_loop()

        OUTLET = StartStream("Polar H9")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run(address, OUTLET))
    ```

Once the LSL Stream is created, it begins broadcasting your physiological sensor data on your computer.

By default, PLUME-Recorder will pick up any live LSL Stream (predicate = `*`) and record it synchronously with your Unity application. If you run multiple LSL streams on the same computer or network, you can filter the streams picked up by PLUME-Recorder by changing the [predicate](https://en.wikipedia.org/w/index.php?title=XPath_1.0&oldid=474981951) in PLUME-Recorder [settings](../recorder/recorded-data/physiological-signals.md).

## Replay physiological signals in-situ
PLUME-Viewer displays recorded physiological data in the replay timeline, in this example it displays the recorded heart rate of the egg hunter.

Following metadata for the signal are also displayed:

* Stream name
* Number of channels
* Acquisition frequency (in Hz)
* Minimum value
* Maximum value

<p align="center">
    <img src="../images/physiological_signal_viewer.png" alt="physiological signal viewer" width="800"/>
</p>

## View physiological signals ex-situ using SigViewer
Export your record as an .xdf file using the following PLUME-Python cli command:

```
plume-python export-xdf path_to_my_record
```

PLUME-Python will export the resulting xdf file next to your record file.

Download the latest release of [SigViewer](https://github.com/cbrnr/sigviewer) and open the created .xdf file.

<p align="center">
    <img src="../images/sigviewer.png" alt="SigViewer" width="800"/>
</p>

Recorded [markers](../recorder/recorded-data/markers.md) are automatically exported as events to be viewed directly within SigViewer.

<p align="center">
    <img src="../images/sigviewer_events.png" alt="SigViewer Events" width="600"/>
</p>
