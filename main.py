# import uvicorn
# import asyncio
# import websockets
# import time
# import multiprocessing
# # from aiomultiprocess import Pool
#
# trigger = False
#
# def let_start():
#     asyncio.create_task(hello())
#
# async def hello():
#     print(1+3)
#
# async def hello1():
#     uri = "ws://192.168.0.101:8765"
#     print("ws--")
#     # while True:
#     async for websocket in websockets.connect(uri, ping_timeout=None):
#         try:
#             # name = input("What's your name? ")
#             #
#             # start = time.perf_counter()
#             await websocket.send("ok")
#             # print(f"> {name}")
#             #
#             # greeting = await websocket.recv()
#             # end = time.perf_counter()
#             # print(f"< {greeting}")
#             # print("Time elapsed during the process:", end - start)
#
#             while True:
#                 global trigger
#                 if trigger:
#                     await websocket.send("true")
#                     time.sleep(10)
#                 else:
#                     await websocket.send("false")
#                     time.sleep(10)
#                 # name = await websocket.recv()
#                 # t_get = time.perf_counter()
#                 print(f"< name")
#
#                 # greeting = f"Hello {name}!"
#                 #
#                 # await websocket.send(greeting)
#                 # print(f"> {greeting}")
#         except websockets.ConnectionClosed:
#             print("continue")
#             continue
#
# def run_app():
#     uvicorn.run("test.app:app", host="0.0.0.0", port=8888, reload=True)
#
# p_ws = multiprocessing.Process(target=let_start)
# p_app = multiprocessing.Process(target=run_app)
#
# # async def pool_process():
# #     async with Pool() as p:
# #         await p.map(run_app,[1])
#
# if __name__ == "__main__":
#     # asyncio.get_event_loop().run_until_complete(pool_process())
#     p_ws.start()
#     # p_app.start()
#     # print("check 1")
#     # asyncio.get_event_loop().run_until_complete(hello())
#     # print("check 2")

from multiprocessing import Process
import uvicorn
import threading

if __name__ == '__main__':
    # uvicorn.run("test.app:app", host="0.0.0.0", port=8888, reload=True)
    uvicorn.run("test.app:app", host="0.0.0.0", port=8811, reload=True)