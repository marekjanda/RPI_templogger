# WEBsocket app to work as a web socket for for data transmission

import asyncio
import websockets
import json
import random

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

def generate_temperatures(temps):
    if not temps:
        return temperatures
    for key in temps:
        temps[key] = random.uniform(70,90)
    return temps

print("Web socket in service")

async def echo(websocket, path):
    async for message in websocket:
        if message == "pull":
            try:
                temperatures = generate_temperatures(temperatures)
            except UnboundLocalError:
                temperatures = generate_temperatures(None)
            
            data = json.dumps(temperatures)
            await websocket.send(data)
            
            temperatures = generate_temperatures(temperatures)

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

