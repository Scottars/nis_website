from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import threading
import socket

import zmq
from zmq.asyncio import Context,ZMQEventLoop
import asyncio
import numpy as np



class realtimeshow_Consumer(AsyncWebsocketConsumer):

    # def __init__(self):
        # self.context = zmq.Context()
        # self.zmqsocketsub1 = self.context(zmq.SUB)
        # print('我们初始化了这个异步的内容')

    async def connect(self):
        self.room_group_name = 'ops_coffee'
        print('we have connected')

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.listening_data()
        # loop = asyncio.get_event_loop()
        # tasks = [self.send_data2front(), self.disconnect()]
        # loop.run_until_complete(asyncio.wait(tasks))
        # loop.close()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = '运维咖啡吧：' + event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    async  def listening_data(self):
        print('we are at linsting data')
        await self.send_data2front()

        # t1 = threading.Thread(target=self.send_data2front)


        # context=Context()
        #
        # zmqsocketsub1 = context(zmq.SUB)
        # print('我们初始化了这个异步的内容')
        # zmqsocketsub1.setsockopt(zmq.SUBSCRIBE,'')
        # zmqsocketsub1.connect(("tcp://127.0.0.1:6555"))
        #
        # await self.get_datafrombackend()




    async def get_datafrombackend(self):
        msg = self.zmqsocketsub1.recv()
        print(msg)
        await self.send_data2front(msg)


    async def send_data2front(self):
        print('we are at send2front')
        i=0
        x = np.arange(0, 2 * np.pi, 0.0001)

        y = np.sin(x)*10
        while i<=len(x)-1:
            i = i + 1
            print('we are in while sleeping')
            await asyncio.sleep(0.01)
            await self.send(str(x[i])+','+str(y[i]))



