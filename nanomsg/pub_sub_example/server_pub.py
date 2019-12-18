from pynng import Pub0,Sub0
import time
from dataservice.datawave_produce.waveproduce import  sin_wave,triangle_wave,swatooth_wave,square_wave
import threading

address='tcp://127.0.0.1:3333'
timeinterval=0.1
def sinpubserver():
    pub=Pub0(dial=address)
    z=1
    zhouqi=10
    periodnum=1
    # x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.01),decimals=2)
    i=0
    x,y=sin_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=0.1,xdecimals=2,ydecimals=5)
    while True:
        # await trio.sleep(1)
        time.sleep(timeinterval)
        print('sending sin ')

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
        pub.send(('sin+'+str(x[i])+','+str(y[i])).encode())
        i = i + 1
        if i>=100:
            i=0
            z= z + 1
            print('z的大小',z)
            x, y = sin_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=0.1, xdecimals=2, ydecimals=5)
def trianglepubserver():
    pub=Pub0(dial=address)
    z=1
    zhouqi=10
    periodnum=1
    # x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.01),decimals=2)
    i=0
    x,y=triangle_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=0.1,xdecimals=2,ydecimals=5)
    while True:
        # await trio.sleep(1)
        time.sleep(timeinterval)
        print('sending triangle ')

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
        pub.send(('triangle+'+str(x[i])+','+str(y[i])).encode())
        i = i + 1
        if i>=100:
            i=0
            z= z + 1
            print('z的大小',z)
            x, y = triangle_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=0.1, xdecimals=2, ydecimals=5)
def squarepubserver():
    pub=Pub0(dial=address)
    z=1
    zhouqi=10
    periodnum=1
    # x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.01),decimals=2)
    i=0
    x,y=sin_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=0.1,xdecimals=2,ydecimals=5)
    while True:
        # await trio.sleep(1)
        time.sleep(timeinterval)
        print('sending square')

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
        pub.send(('square+'+str(x[i])+','+str(y[i])).encode())
        i = i + 1
        if i>=100:
            i=0
            z= z + 1
            print('z的大小',z)
            x, y = square_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=0.1, xdecimals=2, ydecimals=5)

def swatoothpubserver():
    pub=Pub0(dial=address)
    z=1
    zhouqi=10
    periodnum=1
    # x = np.around(np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi + 2 * np.pi, 0.01),decimals=2)
    i=0
    x,y=swatooth_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=0.1,xdecimals=2,ydecimals=5)
    while True:
        # await trio.sleep(1)
        time.sleep(timeinterval)
        print('sending swatooth')
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
        pub.send(('sawtooth+'+str(x[i])+','+str(y[i])).encode())
        i = i + 1

        if i>=100:
            i=0
            z= z + 1
            print('z的大小',z)
            x, y = swatooth_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=0.1, xdecimals=2, ydecimals=5)



if __name__=='__main__':

    tasks=[sinpubserver,trianglepubserver,squarepubserver,swatooth_wave]
    for task in tasks:
        t1=threading.Thread(target=task)
        t1.start()

