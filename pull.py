# Script to get the temperature data from the server and writing into a text file
import asyncio
import websockets
import json

data = {"a":0, "b":1}

async def hello():
    print("Socket active")
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        resp = await websocket.recv()
        print(resp)

asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever(hello)
