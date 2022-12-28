import asyncio
import json
from twilio.rest import Client

async def main():

    with open("private.json", "r") as read_file:
        config = json.load(read_file)

    client = Client(config["twilio-sid"], config["twilio-token"])

    message = client.messages.create(
        to = config["twilio-to"],
        from_ = config["twilio-from"],
        body = "Hello from Python!")

    print(message.sid)

if __name__ == "__main__":
    asyncio.run(main())
