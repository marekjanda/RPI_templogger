# Mockup to generate motor temperature and store in a dict
# All temperatures are in DegC

import asyncio
from json.encoder import JSONEncoder
import websockets
import json
import time

# This definition will come from real temp. monitoring
T01 = 84 
T02 = 85 
T03 = 86
T04 = 82
T05 = 85
T06 = 86
T07 = 82
T08 = 83
T09 = 84
T10 = 80
T11 = 86
T12 = 87

# Create a dictionary that will be pushed to server
temperatures = {
    "T01": T01,
    "T02": T01,
    "T03": T03,
    "T04": T04,
    "T05": T05,
    "T06": T06,
    "T07": T07,
    "T08": T08,
    "T09": T09,
    "T10": T10,
    "T11": T11,
    "T12": T12,
}

# Send temperatures to a server
while True:
    async def hello():
        uri = "ws://localhost:8765"
        async with websockets.connect(uri) as websocket:
            await websocket.send("pull")
            resp = await websocket.recv()
            print(resp)
    
    asyncio.get_event_loop().run_until_complete(hello())
    
    time.sleep(3)
    #asyncio.get_event_loop().run_forever()