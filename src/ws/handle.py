from json import loads, dumps
from ..ids import SERVER_HANDLE, SERVER_USERS

def handle(message: str, server, tui) -> dict:
    """message: 应是json的str形式"""

    message_dict: dict = loads(message) # 处理 message
    result: dict = {}
    match message_dict["com"]:
        case SERVER_HANDLE.JOIN:
            """{com: join, id: user_id, name: user_name}"""
            # 检查是否有存在的用户
            # flag: 是否有存在的用户
            haveSameUser: bool = False
            for user in SERVER_USERS:
                if user["_id"] == message_dict["id"]:
                    result = {
                        "type": "failed",
                        "info": ""
                    }
                    haveSameUser = True
                    break
            # 添加用户
            if not haveSameUser:
                SERVER_USERS.append({
                    "_id": message_dict["id"],
                    "name": message_dict["name"]
                })
                result = {
                    "type": "success",
                    "info": "add user success."
                }
        case _:
            result = {
                "type": "failed",
                "info": "undefined command"
            }
            
    # result: {type: 'failed' | 'success', info: str}
    return {
        "result": dumps(result)
    }