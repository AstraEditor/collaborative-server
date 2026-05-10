from src.ws import WebSocketServer
import asyncio

async def main():
    server = WebSocketServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())