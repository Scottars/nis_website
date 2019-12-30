from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import threading
import socket
from  pynng import Pair1


import asyncio
import numpy as np
from pynng import Pub0,Sub0
address = 'ipc://asyncserverpub'




class realtimeshow_Consumer(AsyncWebsocketConsumer):
    #
    # def __init__(self):
    #
    #     print('我们初始化了这个异步的内容')

    async def connect(self):
        self.room_group_name = 'ops_coffee'
        print('we have connected')

        # Join room group
        # await self.channel_layer.group_add(
        #     self.room_group_name,
        #     self.channel_name
        # )
        await self.accept()
        subscribe_content=[]




    # loop = asyncio.get_event_loop()
        # tasks = [self.send_data2front(), self.disconnect()]
        # loop.run_until_complete(asyncio.wait(tasks))
        # loop.close()

    async def disconnect(self, close_code):
        # Leave room group
        # await self.channel_layer.group_discard(
        #     self.room_group_name,
        #     self.channel_name
        # )
        print('we have disconnected')
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        subscribe_content=[]

        print('we have receive something')
        # print(text_data)
        subscribe_content=text_data.split(',')
        print(subscribe_content)
        await self.listening_data(subscribe_content)





    # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        # print(text_data)
        # #Send message to room group
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message
        #     }
        # )



# Receive message from room group
    async def chat_message(self, event):
        message = '运维咖啡吧：' + event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    async  def listening_data(self,subscribe_content):
        print('we are at linsting data')
        # await self.send_data2front()
        # t1 = threading.Thread(target=self.send_data2front)
        # topic=
        sub1 = Sub0(dial=address)
        # print(subscribe_content)
        # sub1.subscribe(subscribe_content)
        # sub1.subscribe(b'sawtooth')
        # subscribe_content=[]
        if len(subscribe_content)==0:
            sub1.subscribe(b'')
        else:

            for subtopic in subscribe_content:
                print(subtopic)
                sub1.subscribe(subtopic)


        # 突然想到还是采用多个pub 多个sub 以及 中间的代理部分
        # 如何启动这些内容
        # 如果多个不同的地方分布到不同的前台的界面，相应速度是否会收到影响。

        ###发送多个数据
        # while True:
        #     msg =await sub1.arecv()
        #     msg = msg.decode()
        #     # self.send(msg)
        #     name, data = msg.split('+')
        #     jsondata = {
        #         name: data.split('=')  # 这个是启用多个数据一起发送的方案
        #     }
        #     a = json.dumps(jsondata)
        #     print('we are in d多个数据发送')
        #     print(a)
        #
        #     await self.send(a)
        #     print('发送成功了 啊')





        ###发送单个数据
        while True:
            msg = await sub1.arecv()
            print('发送单个数据')

            msg=msg.decode()
            name,data=msg.split('+')
            jsondata={
                name:data.split(',') #单个数据发送方案
            }
            a = json.dumps(jsondata)
            print(a)

            await self.send(str(a))

#下面是同步的写法，由于用到了channel——layer，所以一切都变成了异步，而因此，我们必须讲异步的通信消息，编程同步的内容
class syncrealtimetConsumer(WebsocketConsumer):


    def connect(self):
        self.room_group_name = 'ops_coffee'
        print('we are here1')
        # Join room group
        # async_to_sync(self.channel_layer.group_add)(   #ps 这一部分是使用channel的，使用这一部分是为了使得所有其他的
        #     self.room_group_name,                      #webclient都能收到来自同一个地方的数据
        #     self.channel_name
        # )
        # print('we are here2')
        self.accept()
        # self.chat_message()

    def disconnect(self, close_code):
        # Leave room group
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        pass

    # Receive message from WebSocket
    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        self.realtime_multidata()

        # Send message to room group
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message
        #     }
        # )

    # Receive message from room group
    def chat_message(self):
        sub1 = Sub0(dial=address)
        sub1.subscribe(b'')
        print('we are at chatmsg')
        # 突然想到还是采用多个pub 多个sub 以及 中间的代理部分
        # 如何启动这些内容
        # 如果多个不同的地方分布到不同的前台的界面，相应速度是否会收到影响。
        while True:
            msg = sub1.recv()
            msg=msg.decode()
            name,data=msg.split('+')
            jsondata={
                name:data.split(',')
            }
            a = json.dumps(jsondata)
            print(type(a))
            # print(jsondata['sin'])

            self.send(str(a))
    def realtime_multidata(self):
        sub1 = Sub0(dial=address)
        sub1.subscribe(b'sin')
        print('we are at realtine')
        # 突然想到还是采用多个pub 多个sub 以及 中间的代理部分
        # 如何启动这些内容
        # 如果多个不同的地方分布到不同的前台的界面，相应速度是否会收到影响。
        while True:
            msg = sub1.recv()
            msg=msg.decode()
            name,data=msg.split('+')
            jsondata={
                name:data.split('=')   #这个是启用多个数据一起发送的方案
            }
            a = json.dumps(jsondata)
            print(type(a))
            print(a)

            self.send(str(a))