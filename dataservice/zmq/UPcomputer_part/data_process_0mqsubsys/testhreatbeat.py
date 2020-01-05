import  zmq

#两种方案:
# 1. 守护进程定时访问,收到被守护进程的反馈
# 2. 被监控的进程定时发送一条alive的消息
#考虑的需求点
#1.进程是否运行的消息是最好要返回到web上面

#结论:
#A:web可以主动的点击通过按钮进行对被守护进程的访问,
#B: 主动定时:低频率


#采用的套接字:req_rep
#唯一的表示:端口号不同
import datetime
import threading
import zmq
import time

def fun_timer1(url):


    print('we are here in function')
    client = context.socket(zmq.REP)
    # client.RCVTIMEO = 1000*3
    client.bind(url)

    # client.setsockopt()
    while True:
        print(client.recv())
        client.send(b'I am alive  '+ url.encode())


#定时脚本
if __name__ == '__main__':
    # t1=threading.Timer(3, task)
    # t1.start()
    context=zmq.Context()
    for i in range(9):
        url = 'tcp://127.0.0.1:700'+ str(i)
        print(url)

        t1 = threading.Thread(target=fun_timer1,args={url})
        t1.start()

    # t2 = threading.Thread(target=fun_timer2,args=(context,url))
    # t2.start()

    print('we are here')


    # fun_timer2()



#










