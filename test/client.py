import datetime
import asyncio
import websockets
import time

check_online = 30
trigger = False
payload_data = None
update_time_rec = None

def let_start():
    asyncio.create_task(hello())

async def is_online():
    time_now = datetime.datetime.now()
    if update_time_rec:
        time_diff = time_now - update_time_rec
        if int(time_diff.total_seconds()) < check_online:
            return True
        else:
            return False
    else:
        return False


async def trigger_func():
    global trigger
    print("before: ", trigger)
    trigger = not trigger
    print("after: ", trigger)

async def set_payload(data):
    global payload_data
    global trigger
    print("before: ", trigger)
    trigger = True
    print("after: ", trigger)
    payload_data = data

async def send_payload(ws_in):
    global trigger
    while True:
        if trigger:
            trigger = False
            await ws_in.send(payload_data)
        await asyncio.sleep(3)


async def hello():
    uri = "ws://192.168.0.101:8000/ws"
    print("ws--", uri)
    async for websocket in websockets.connect(uri, ping_timeout=None):
        try:
            await websocket.send("ok")
            while True:
                global trigger
                global update_time_rec
                send_text = asyncio.create_task(send_payload(websocket))
                recv_data = await websocket.recv()
                send_text.cancel()
                update_time_rec = datetime.datetime.now()
                print(recv_data)
        except websockets.ConnectionClosed:
            print("continue")
            continue
    print("at the end of ws")