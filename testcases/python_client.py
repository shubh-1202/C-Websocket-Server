import asyncio
import websockets
async def test():
    async with websockets.connect('ws://localhost:10000') as websocket:
        await websocket.send("hello I am robot")
        response = await websocket.recv()
        print(response)
asyncio.get_event_loop().run_until_complete(test())

