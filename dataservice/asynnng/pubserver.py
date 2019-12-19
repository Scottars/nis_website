import time
import numpy as np
from pynng import Pub0, Sub0, Timeout,Pair0   #Pair0 可以用来同步服务器和客户端，来保证了  只有同步了才能继续发送数据
import asyncio
import pymysql
from dataservice.datawave_produce.waveproduce import sin_wave,triangle_wave,square_wave,sawtooth_wave
address = 'tcp://127.0.0.1:3333'
timeinterval=0.1

def pubserver():
    pub=Pub0(dial=address)
    i = 1
    while True:
        i = i + 1
        time.sleep(1)
        print('we are sending-----')
        pub.send(b'asyn masg')
async def pubserverasyn():
    pub=Pub0(dial=address)

    db = pymysql.connect(host='localhost', user='root', password='123456', db='test', port=3306, charset='utf8')
    cur = db.cursor()
    i = 0
    while True:
        # await trio.sleep(1)
        await asyncio.sleep(0.1)
        print('we are reading--data---')

        sql = 'select * from sinvalue order by id DESC limit 1;'
        cur.execute(sql)  # 选择需要读取的数据
        db.commit()  #db commit 确定提交这条记录 否则，每次执行的时候，返回都是第一次自信的结果。如果要获取最新的一条的数据，需要使用db.commit 对其进行提交
        data = cur.fetchall()  # 对读取到的数据赋值为data
        print(data)
        await pub.asend((str(data[0][1])+','+str(data[0][2])).encode())
        # i = i + 1
        # if i==63:
        #     i=0
        #     Z= Z + 1
        #     print('z的大小',Z)
        #     x = np.arange((Z - 1) *  2 * np.pi,(Z - 1) *  2 * np.pi+ 2 * np.pi, 0.1)
        #
        #     y = np.sin(x) * 100
async def sinpubserverasynori():
    pub=Pub0(dial=address)
    z=1
    zhouqi=10
    periodnum=1
    # x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.01),decimals=2)
    i=0
    x,y=sin_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=0.1,xdecimals=2,ydecimals=5)
    while True:
        # await trio.sleep(1)
        await asyncio.sleep(timeinterval)
        print('we are sending ')

#多个数据一起上传
        # msg=''
        # for j in range (10):
        #     msg = msg +str(x[i])+','+str(y[i])+'='
        #     i = i + 1
        #     if i >= 62:
        #         i = 0
        #         Z = Z + 1
        #         print('z的大小', Z)
        #
        #         x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.1), decimals=2)
        #
        #         y = np.around(np.sin(x) * 100, decimals=5)
        #
        # print(msg)
        # # print(data)
        # await pub.asend(msg.encode())
#单个数据独立上传
     # print(data)
        await pub.asend(('sin+'+str(x[i])+','+str(y[i])).encode())
        i = i + 1
        if i>=100:
            i=0
            z= z + 1
            print('z的大小',z)
            x, y = sin_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=0.1, xdecimals=2, ydecimals=5)
async def trianglepubserverasynori():
    pub=Pub0(dial=address)
    z=1
    zhouqi=10
    periodnum=1
    # x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.01),decimals=2)
    i=0
    x,y=triangle_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=0.1,xdecimals=2,ydecimals=5)
    while True:
        # await trio.sleep(1)
        await asyncio.sleep(timeinterval)
        print('we are sending ')

#多个数据一起上传
        # msg=''
        # for j in range (10):
        #     msg = msg +str(x[i])+','+str(y[i])+'='
        #     i = i + 1
        #     if i >= 62:
        #         i = 0
        #         Z = Z + 1
        #         print('z的大小', Z)
        #
        #         x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.1), decimals=2)
        #
        #         y = np.around(np.sin(x) * 100, decimals=5)
        #
        # print(msg)
        # # print(data)
        # await pub.asend(msg.encode())
#单个数据独立上传
     # print(data)
        await pub.asend(('triangle+'+str(x[i])+','+str(y[i])).encode())
        i = i + 1
        if i>=100:
            i=0
            z= z + 1
            print('z的大小',z)
            x, y = triangle_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=0.1, xdecimals=2, ydecimals=5)
async def squarepubserverasynori():
    pub=Pub0(dial=address)
    z=1
    zhouqi=10
    periodnum=1
    # x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.01),decimals=2)
    i=0
    x,y=sin_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=0.1,xdecimals=2,ydecimals=5)
    while True:
        # await trio.sleep(1)
        await asyncio.sleep(timeinterval)
        print('we are sending ')

#多个数据一起上传
        # msg=''
        # for j in range (10):
        #     msg = msg +str(x[i])+','+str(y[i])+'='
        #     i = i + 1
        #     if i >= 62:
        #         i = 0
        #         Z = Z + 1
        #         print('z的大小', Z)
        #
        #         x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.1), decimals=2)
        #
        #         y = np.around(np.sin(x) * 100, decimals=5)
        #
        # print(msg)
        # # print(data)
        # await pub.asend(msg.encode())
#单个数据独立上传
     # print(data)
        await pub.asend(('square+'+str(x[i])+','+str(y[i])).encode())
        i = i + 1
        if i>=100:
            i=0
            z= z + 1
            print('z的大小',z)
            x, y = square_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=0.1, xdecimals=2, ydecimals=5)

async def sawtoothpubserverasynori():
    pub=Pub0(dial=address)
    z=1
    zhouqi=10
    periodnum=1
    # x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.01),decimals=2)
    i=0
    x,y=swatooth_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=0.1,xdecimals=2,ydecimals=5)
    while True:
        # await trio.sleep(1)
        await asyncio.sleep(timeinterval)
        print('we are sending ')

#多个数据一起上传
        # msg=''
        # for j in range (10):
        #     msg = msg +str(x[i])+','+str(y[i])+'='
        #     i = i + 1
        #     if i >= 62:
        #         i = 0
        #         Z = Z + 1
        #         print('z的大小', Z)
        #
        #         x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.1), decimals=2)
        #
        #         y = np.around(np.sin(x) * 100, decimals=5)
        #
        # print(msg)
        # # print(data)
        # await pub.asend(msg.encode())
#单个数据独立上传
     # print(data)
        await pub.asend(('sawtooth+'+str(x[i])+','+str(y[i])).encode())
        i = i + 1
        if i>=100:
            i=0
            z= z + 1
            print('z的大小',z)
            x, y = sawtooth_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=0.1, xdecimals=2, ydecimals=5)




async def subclient():
    sub1 = Sub0(dial=address, recv_timeout=100)
    sub1.subscribe(b'')
    i = 1
    while True:
        i = i + 1
        msg= await sub1.arecv()
        print('收到的内容',msg)


if __name__=='__main__':

    tasks = [asyncio.ensure_future(sawtoothpubserverasynori()),asyncio.ensure_future(sinpubserverasynori()),asyncio.ensure_future(trianglepubserverasynori()),asyncio.ensure_future(squarepubserverasynori())]
    # tasks = [asyncio.ensure_future(trianglepubserverasynori())]


    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


    import trio
    # pubserver()
    # mainwork()
    # trio.run(pubserverasyn)

