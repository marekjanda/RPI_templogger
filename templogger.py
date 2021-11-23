# Mockup to generate motor temperature and store in a dict
# All temperatures are in DegC

import asyncio
import websockets
import json
import time
import socket
import datetime

logging_timne = 5 #Seconds
rpi_address = socket.gethostbyname('raspberrypi')
print(f"RPI IP ADDRESS: {rpi_address}")

def log_to_txt(temps):
    '''Writes logged temperatures into a text file'''
    with open("motor_temps.txt", 'w', encoding='utf-8') as f:
        for t in temps:
            if t == "T12":
                f.write(f"{temps[t]}")
            else:
                f.write(f"{temps[t]}\n")
    return

# Pull temperatures to a server
try_count = 0
while True:
    async def logger():
        global try_count
        '''Pulls temperatures from the RPI websocket'''
        uri = f"ws://{rpi_address}:8765" #localhost to be replaced by RPI IP address (laptop IP 10.103.131.227)
        
        try:
            async with websockets.connect(uri) as websocket:
                await websocket.send("pull")
                resp = await websocket.recv()
                temperatures = json.loads(resp)
                print(temperatures)
                log_to_txt(temperatures)
                try_count = 0
                         
        except OSError:
            try_count += 1
            print(f"{datetime.datetime.now()}: Semaphore timeout - Try No. {try_count}")
            if try_count == 5:
                print("Could not establish connection")
                raise ConnectionError
    
    asyncio.get_event_loop().run_until_complete(logger())
    
    time.sleep(logging_timne)
    #asyncio.get_event_loop().run_forever()