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
        self.host: str = host
        self.port: int = port
        self.tui = tui or (lambda: None) # 因为对于lambda加类型注解有点麻烦了，总之你知道这是lambda

        self.project_data: str = ""
    
    async def handler(self, websocket) -> None:
        async for message in websocket:
            getBack = handle(message=message, server=self, tui=self.tui)
            # 刷新tui
            self.tui._refresh_users() # type: ignore
            await websocket.send(str(getBack["result"]))

    async def start_server(self) -> None:
        """开启服务器"""
        async with websockets.serve(handler=self.handler, host=self.host, port=self.port):
            await asyncio.Future()

    async def run(self) -> None:
        # main
        await self.start_server()
