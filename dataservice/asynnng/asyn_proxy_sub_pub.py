import time
import numpy as np
from pynng import Pub0, Sub0, Timeout,Pair0   #Pair0 可以用来同步服务器和客户端，来保证了  只有同步了才能继续发送数据
import asyncio
import pymysql
from dataservice.datawave_produce.waveproduce import sin_wave,triangle_wave,square_wave,sawtooth_wave
addresssub = 'tcp://127.0.0.1:3333'
addresspub = 'tcp://127.0.0.1:3334'

async def proxy_subpub():
    sub_sock = Sub0(listen=addresssub)
    sub_sock.subscribe(b'')

    pub_sock = Pub0(listen=addresspub)
    while True:
        print('we are receiving')
        msg = sub_sock.recv()
        print(msg)
        pub_sock.send(msg)



if __name__=='__main__':

    tasks = [asyncio.ensure_future(proxy_subpub())]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


    import trio
    # pubserver()
    # mainwork()
    # trio.run(pubserverasyn)

