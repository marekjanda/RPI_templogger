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

rpi_address = '10.103.131.227' #This is J&E laptop IP, needs to be replaced with RPI address or localhost

def generate_temperatures(temps):
    if not temps:
        return temperatures
    for key in temps:
        temps[key] = round(random.uniform(70,90),2)
    return temps

print("Web socket in service")

async def echo(websocket, path):
    async for message in websocket:
        print(f"Pull request: {websocket}")
        if message == "pull":
            try:
                temperatures = generate_temperatures(temperatures)
            except UnboundLocalError:
                temperatures = generate_temperatures(None)
            
            data = json.dumps(temperatures)
            print(data) 
            await websocket.send(data)
            
            temperatures = generate_temperatures(temperatures)

start_server = websockets.serve(echo, rpi_address, 8765) #localhost to be replaced by RPI IP address (laptop IP 10.103.131.227)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

