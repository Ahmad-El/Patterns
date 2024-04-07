import asyncio
import websockets
import keyboard
import time
async def start_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        done = False
        while not done:
            # if keyboard.is_pressed("space"):
            time.sleep(5) 
            await websocket.send("buzz")
            message = await websocket.recv()
            print(message)
            done = True
        
asyncio.run(start_client())