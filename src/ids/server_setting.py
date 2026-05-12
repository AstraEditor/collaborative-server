from typing import TypedDict
# 成员表
class Users(TypedDict):
    _id: str
    name: str
SERVER_USERS:list[Users] = []

SERVER_SETTING = {
    "IP": "localhost",
    "DEFAULTPORT": 1832,
}