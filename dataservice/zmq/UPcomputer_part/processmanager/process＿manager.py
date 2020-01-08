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
# import lock
RCV_TIMEOUT= 1000*3
lock= threading.Lock()

def fun_timer1(url,process_name):



    # 定义全局变量
    # global timer
    # 10秒调用函数一次
    # timer = threading.Timer(5, fun_timer1,(context,url))
    # # 启用定时器
    # timer.start()
    print('we are here in function')
    print(process_name)


    client = socket_REQ_Conenct(url)


# client.setsockopt()
    while True:



        try:
            client.send(b'Are you alive')
            # print('we have send to ')
            msg= client.recv()
            print(msg)


            sql = "UPDATE data_process_ipc SET process_status = 'on' WHERE process_name = '%s'" % (process_name)
            lock.acquire()
            cur.execute(sql)
            db.commit()
            lock.release()
            # lock.unlock()
            db.commit()
            time.sleep(10)
            ###成功
            '''
            '''
        except zmq.error.Again:  #接收超时异常
            sql = "UPDATE data_process_ipc SET process_status = 'off' WHERE process_name = '%s'" % (process_name)

            # sql = "INSERT INTO data_process_ipc (process_name,process_status,update_time) values ('data_process_03_vacuumm_num2','off',NOW())"
            lock.acquire()
            cur.execute(sql)
            db.commit()
            lock.release()

            print('we are having error')
            # client.connect(url)
            '''
            
            
            '''
            client.close()
            # print(3)

            client= socket_REQ_Conenct(url)

def socket_REQ_Conenct(url):
    # print(url + ' connecting...')
    client = context.socket(zmq.REQ)
    client.setsockopt(zmq.LINGER, 10)
    client.RCVTIMEO = RCV_TIMEOUT
    client.connect(url)

    return client

        # try:
        #     time.sleep(2)
        #     print('we are at function1')

def fun_timer2(context,url):
    # print('time2',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #k
    # # 定义全局变量
    # # global timer
    # # 10秒调用函数一次
    # timer = threading.Timer(1, fun_timer2)
    # # 启用定时器
    # timer.start()
    while True:
        time.sleep(2)
        print('we are at function2')


import pymysql
#定时脚本
if __name__ == '__main__':
    # t1=threading.Timer(3, task)
    # t1.start()
    context=zmq.Context()

    db = pymysql.connect(host='localhost', user='scottar', password='123456', db='nis_hsdd', port=3306, charset='utf8')
    cur = db.cursor()

    #
    #
    process_names =['process_02_watercooldown_num10','process_03_vacuumm_num2','process_04_cesium_num5',
                   'process_05_gascontrol_num3','process_06_pgmagneticpower_num2',
                   'process_07_filament_num4','process_08_RFpower_num1',
                   'process_10_leadingoutpower_num2','process_11_acceleratepower_num2'
                   ]

    urls = ['tcp://127.0.0.1:8002','tcp://127.0.0.1:8003','tcp://127.0.0.1:8004','tcp://127.0.0.1:8005','tcp://127.0.0.1:8006','tcp://127.0.0.1:8007','tcp://127.0.0.1:8008','tcp://127.0.0.1:8010','tcp://127.0.0.1:8011']
    #
    for i in range(9):
    # print(urls[i])
    # print(process_names[i])
    #     sql = "INSERT INTO data_process_ipc (process_name,process_status,update_time) values ('%s','off',NOW())" % (process_names[i])
    #     cur.execute(sql)
    #     db.commit()

        t1 = threading.Thread(target=fun_timer1,args=(urls[i],process_names[i]))
        t1.start()

    #
    # t1 = threading.Thread(target=fun_timer1,args=(urls[0],process_names[0]))
    # t1.start()
    # t1 = threading.Thread(target=fun_timer1,args=(urls[1],process_names[1]))
    # t1.start()
    # t1 = threading.Thread(target=fun_timer1,args=(urls[2],process_names[2]))
    # t1.start()
    # t1 = threading.Thread(target=fun_timer1,args=(urls[3],process_names[3]))
    # t1.start()
    # fun_timer2()



#










