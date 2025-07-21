import asyncio
import websockets

async def connect(uri: str):
    async with websockets.connect(uri) as websocket:
        await websocket.send("hello")
        response = await websocket.recv()
        print(f"Server replied: {response}")

if __name__ == "__main__":
    asyncio.run(connect("ws://localhost:8765"))
