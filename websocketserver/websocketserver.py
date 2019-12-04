#!/usr/bin/python3

import websockets
import asyncio
import time
global i
i=1

async def hello(websocket, path):
    # name = await websocket.recv()
    # print(f"A new client : {name}")
    # greeting = "Welcome " + name
    # time.sleep(2)
    global i


    for j in range(100):
        i = i + 1
        data= str(i)+','+str(i)
        await websocket.send(data)
        time.sleep(1)
        print(data)
    # await websocket.send("2,2")
    # print(f"send '{greeting}' to '{name}'")


start_server = websockets.serve(hello, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


