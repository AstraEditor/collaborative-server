from json import loads, dumps
from ..ids import SERVER_HANDLE

def handle(message, self) -> dict:
    """message: 应是json的str形式"""

    message = loads(message) # 处理 message
    result: dict = {}
    match message["com"]:
        case SERVER_HANDLE.JOIN:
            """{com: join, id: user_id, name: user_name}"""
            # 检查是否有存在的用户
            for user in self.users:
                if user["id"] == message["id"]:
                    result = {
                        "type": "failed",
                        "info": ""
                    }
    # result: {type: 'failed' | 'success', info: str}
    return {
        "result": dumps(result)
    }