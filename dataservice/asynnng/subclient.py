import time
from pynng import Pub0, Sub0, Timeout
import asyncio
address = 'tcp://127.0.0.1:31313'

async def subclientasyn():
    sub1 = Sub0(dial=address)
    sub1.subscribe(b'')
    i = 1
    while True:
        i = i + 1
        msg= await sub1.arecv()
        print('收到的内容',msg)
def subclient():
    sub1 = Sub0(dial=address)
    sub1.subscribe(b'')
    i = 1
    while True:
        msg=sub1.recv()
        print('收到的内容',msg)
if __name__=='__main__':
    # import trio
    # subclient()

    # trio.run(subclientasyn)
    tasks = [asyncio.ensure_future(subclientasyn())]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()




