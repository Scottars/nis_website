import time
from pynng import Pub0, Sub0, Timeout
import asyncio
address = 'tcp://127.0.0.1:31313'

def pubserver():
    pub=Pub0(listen=address)
    i = 1
    while True:
        i = i + 1
        time.sleep(1)
        print('we are sending-----')
        pub.send(b'asyn masg')
async def pubserverasyn():
    pub=Pub0(listen=address)
    i = 1
    while True:

        i = i + 1
        # await trio.sleep(1)
        await asyncio.sleep(1)
        print('we are sending-----')
        await pub.asend(str(i).encode())
async def subclient():
    sub1 = Sub0(dial=address, recv_timeout=100)
    sub1.subscribe(b'')
    i = 1
    while True:
        i = i + 1
        msg= await sub1.arecv()
        print('收到的内容',msg)


if __name__=='__main__':
    import trio
    # pubserver()
    tasks = [asyncio.ensure_future(pubserverasyn())]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    # trio.run(pubserverasyn)

