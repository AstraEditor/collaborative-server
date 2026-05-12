import asyncio
import websockets
from typing import TypedDict, Literal

from .handle import handle
from ..ids import SERVER_SETTING


class WebSocketServer:
    def __init__(
            self,
            host: str = SERVER_SETTING["IP"],
            port: int = SERVER_SETTING["DEFAULTPORT"],
            tui = lambda: None
    ) -> None:
        self.host = host
        self.port = port
        self.tui = tui or (lambda: None) # 因为对于lambda加类型注解有点麻烦了，总之你知道这是lambda

        self.messages: list[dict] = []

        class Users(TypedDict):
            _id: str # LTY说会和id命令装，故更改
            name: str
            join_time: int
            permiss: Literal["ghost", "op"] # 🦐强强
        self.users: list[Users] = []

        self.project_data: str = ""
    
    async def handler(self, websocket) -> None:
        async for message in websocket:
            getBack = handle(message, self)
            if self.tui._refresh_users(): self.tui._refresh_users() # type: ignore
            await websocket.send(str(getBack["result"]))

    async def start_server(self) -> None:
        """开启服务器"""
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()

    async def run(self):
        # main
        await self.start_server()