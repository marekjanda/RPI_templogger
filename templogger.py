# Mockup to generate motor temperature and store in a dict
# All temperatures are in DegC

import asyncio
import websockets
import json
import time

def log_to_txt(temps):
    with open("motor_temps.txt", 'w', encoding='utf-8') as f:
        for t in temps:
            if t == "T12":
                f.write(f"{temps[t]}")
            else:
                f.write(f"{temps[t]}\n")
    return

# Pull temperatures to a server
while True:
    async def hello():
        uri = "ws://localhost:8765"
        async with websockets.connect(uri) as websocket:
            await websocket.send("pull")
            resp = await websocket.recv()
            temperatures = json.loads(resp)
            print(temperatures)
            log_to_txt(temperatures)
    
    asyncio.get_event_loop().run_until_complete(hello())
    
    time.sleep(3)
    #asyncio.get_event_loop().run_forever()