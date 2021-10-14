from fastapi import WebSocket

from typing import Dict

# from .connection import official_devices

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket] = {}

    async def connect(self, sorter_id, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[sorter_id] = websocket

    def disconnect(self, sorter_id):
        self.active_connections.pop(sorter_id)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()


async def get_match_device_info(m_a):
    # data_get = await official_devices.find_one({"hash_mac": m_a})
    data_get = "12345"
    if data_get:
        # return data_get["device_id"]
        return data_get
    else:
        return None


