import asyncio
import json
import time
from random import randrange
from azure.iot.device.aio import IoTHubDeviceClient

def get_temp():
    return randrange(10)

async def main():

    with open("private.json", "r") as read_file:
        config = json.load(read_file)

    device_client = IoTHubDeviceClient.create_from_connection_string(config["connection-string"])
    await device_client.connect()

    last_temp = ""

    done = False
    sample_count = 0
    max_samples = 64

    while not (done):
        temp = "{0:0.1f}".format(get_temp())
        print("data", temp)

        if temp != last_temp:
            last_temp = temp;

            data = {}
            data['sample'] = temp
            json_body = json.dumps(data)
            print("Sending message: ", json_body)
            sample_count += 1
            await device_client.send_message(json_body)

        done = (sample_count > max_samples)

        time.sleep(30)

    await device_client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
