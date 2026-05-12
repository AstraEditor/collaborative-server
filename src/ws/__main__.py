from src.ws import WebSocketServer
import asyncio

async def main(tui = lambda: None) -> None:
    server = WebSocketServer(tui = tui)
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())