import time
import numpy as np
from pynng import Pub0, Sub0, Timeout,Pair0   #Pair0 可以用来同步服务器和客户端，来保证了  只有同步了才能继续发送数据
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
    # i=0

    # while i<=len(x)-1:
    #     i = i + 1
    #     print('we are in while sleeping')
    #     await asyncio.sleep(1)
    Z=1

    x = np.arange((Z-1)*2*np.pi, 2 * np.pi, 0.1)

    y = np.sin(x)*100
    i = 0
    while True:


        # await trio.sleep(1)
        await asyncio.sleep(0.1)
        print('we are sending-----')
        await pub.asend((str(x[i])+','+str(y[i])).encode())
        i = i + 1
        if i==63:
            i=0
            Z= Z + 1
            print('z的大小',Z)
            x = np.arange((Z - 1) *  2 * np.pi,(Z - 1) *  2 * np.pi+ 2 * np.pi, 0.1)

            y = np.sin(x) * 100
async def subclient():
    sub1 = Sub0(dial=address, recv_timeout=100)
    sub1.subscribe(b'')
    i = 1
    while True:
        i = i + 1
        msg= await sub1.arecv()
        print('收到的内容',msg)


if __name__=='__main__':

    tasks = [asyncio.ensure_future(pubserverasyn())]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


    import trio
    # pubserver()
    # mainwork()
    # trio.run(pubserverasyn)
