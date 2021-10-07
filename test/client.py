import datetime
import asyncio
import websockets
import time

check_online = 30
update_time_rec = None
is_error = False
ws_conn = None

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
    print("payload data: ", payload_data)
    await ws_conn.send(data)


async def send_payload(ws_in):
    global trigger, is_error
    try:
        while True:
            if trigger:
                trigger = False
                await ws_in.send(payload_data)
                # await ws_in.send("{'message':'hey hey yo yo'}")
            await asyncio.sleep(1)
    except Exception as e:
        print("e: ", e)
        trigger = True
        is_error = True


async def hello():
    uri = "ws://192.168.0.101:8000/ws"
    print("ws--")
    async for websocket in websockets.connect(uri, ping_timeout=None):
        try:
            global ws_conn
            ws_conn = websocket
            # asyncio.create_task(send_payload(websocket))
            # await websocket.send("ok")
            while True:
                print("inside while")
                global trigger
                global update_time_rec
                send_text = 10
                recv_data = await websocket.recv()
                update_time_rec = datetime.datetime.now()
                print(recv_data)
                # send_text.cancel()
                if is_error:
                    break
        except (websockets.ConnectionClosed, websockets.ConnectionClosedOK):
            print("reconnecting...")
            continue
    print("at the end of ws")