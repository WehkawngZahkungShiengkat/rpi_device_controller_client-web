from fastapi import FastAPI, Body
from test.client import let_start, trigger_func, set_payload, is_online
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from enum import Enum
# from fastapi.testclient import TestClient
import asyncio
import websockets
import time
import multiprocessing

app = FastAPI()

trigger = False

#----------- Schema start -----------
class StatusValue(str, Enum):
    run = "run"
    stop = "stop"

class LonganSize(str, Enum):
    A = "A"
    AA = "AA"
    B = "B"

class ControlValue(BaseModel):
    function: bool = Field(...)

class ControlValueWithPercent(BaseModel):
    percentage: int = Field(...)
    function: bool = Field(...)

class SorterSetting(BaseModel):
    longan_size: LonganSize = Field(...)
    broken: ControlValue = Field(...)
    seed: ControlValue = Field(...)
    hole_stem: ControlValue = Field(...)
    hole_body: ControlValue = Field(...)
    dent: ControlValueWithPercent = Field(...)
    dirty: ControlValueWithPercent = Field(...)
    # fungi: ControlValue = Field(...)
    # fracture: ControlValue = Field(...)

    class Config:
        allow_population_by_field_name = True

class SorterControl(BaseModel):
    device_name: str = Field(...)
    status: StatusValue = Field(...)
    default: bool = Field(False)
    setting: SorterSetting = Field(...)

    class Config:
        allow_population_by_field_name = True


@app.on_event("startup")
async def startup_sequence():
    let_start()

@app.get("/")
async def homepage():
    online_status = await is_online()
    print("online_status")
    return {"is_online": online_status}

@app.post("/ok")
async def post_ok(req: SorterControl = Body(...)):
    d_rec = jsonable_encoder(req)
    print("type1: ", type(req))
    print("d_rec: ", d_rec)
    ws_data = {"status": d_rec["status"], "setting": d_rec["setting"]}
    await set_payload(str(ws_data))
    return d_rec
# def test_websocket():
#     # client = TestClient(app)
#     with client.websocket_connect("ws://192.168.0.101:8765") as websocket:
#         data = websocket.send_text("hello")
#         # assert data == {"msg": "Hello WebSocket"}
