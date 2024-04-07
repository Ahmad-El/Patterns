import asyncio
import websockets

clients = []

async def handle_message(websocket, path):
    global clients
    global fastests_time 
    message = await websocket.recv()
    if message == 'buzz':
        response_time = asyncio.get_event_loop().time()
        clients.append([websocket, response_time])
        if len(clients) == 1:
            await websocket.send("First Place")
            fastests_time = response_time
        else:
            t = round(response_time - fastests_time, 2)
            await websocket.send(f"Responce time: {t} sec. slower")
    
async def start_server():
    async with websockets.serve(handle_message, "localhost", 8765):
        await asyncio.Future()
        
        
asyncio.run(start_server())