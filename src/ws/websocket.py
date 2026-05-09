import asyncio
import websockets
from typing import TypedDict

from .handle import handle


class WebSocketServer:
    def __init__(
            self,
            host: str = 'localhost',
            port: int = 1983
    ):
        self.host = host
        self.port = port

        self.messages: list[dict] = []

        class Users(TypedDict):
            id: str
            name: str
            join_time: int
            permiss: str # "ghost" | "op"
        self.users: list[Users] = []

        self.project_data: str = ""
    
    async def handler(self, websocket):
        async for message in websocket:
            getBack = handle(message, self)
            await websocket.send(getBack["result"])

    async def start_server(self):
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()

    def run(self):
        asyncio.run(self.start_server())