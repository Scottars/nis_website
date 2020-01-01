
import pymysql
import numpy as np
from dataservice.datawave_produce.waveproduce import sin_wave,triangle_wave,sawtooth_wave,square_wave



# database connect
db = pymysql.connect(host='localhost', user='root', password='123456', db='nis_hsdd', port=3306, charset='utf8')
cur = db.cursor()

import time

start_time = time.process_time()

z=1
zhouqi=6
glo_midu=0.1

zongshu=100
# x = np.arange((Z - 1) * 2 * np.pi, 2 * np.pi, 0.1)

x,y=triangle_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=glo_midu,xdecimals=2,ydecimals=5)

j=0
for i in range(zongshu):
    time.sleep(0.000001)

    print('we are saving')
    sql = "INSERT INTO  v_data_monitor(subsys_id,register_id,exp_id,v_data,v_data_time) values (5,1,1,%f,NOW(6));" % (y[j])
    cur.execute(sql)
    db.commit()
    j = j + 1
    # i = i + 1
    if j>=zhouqi/glo_midu:
        j=0
        z= z + 1
        print('z的大小',z)
        x, y = triangle_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=glo_midu, xdecimals=2, ydecimals=5)

end_time = time.process_time()
print(end_time-start_time)
# print(b[2])

z=1
zhouqi=6
glo_midu=0.1
x,y=sin_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=glo_midu,xdecimals=2,ydecimals=5)

j=0
for i in range(zongshu):
    time.sleep(0.000001)

    print('we are saving')
    sql = "INSERT INTO  v_data_monitor(subsys_id,register_id,exp_id,v_data,v_data_time) values (5,2,1,%f,NOW(6));" % (y[j])
    cur.execute(sql)
    db.commit()
    j = j + 1
    # i = i + 1
    if j>=zhouqi/glo_midu:
        j=0
        z= z + 1
        print('z的大小',z)
        x, y = sin_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=glo_midu, xdecimals=2, ydecimals=5)


z=1
zhouqi=6
glo_midu=0.1
x,y=square_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=glo_midu,xdecimals=2,ydecimals=5)

j=0
for i in range(zongshu):
    time.sleep(0.000001)

    print('we are saving')
    sql = "INSERT INTO  v_data_monitor(subsys_id,register_id,exp_id,v_data,v_data_time) values (5,3,1,%f,NOW(6));" % (y[j])
    cur.execute(sql)
    db.commit()
    j = j + 1
    # i = i + 1
    if j>=zhouqi/glo_midu:
        j=0
        z= z + 1
        print('z的大小',z)
        x, y = square_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=glo_midu, xdecimals=2, ydecimals=5)



z=1
zhouqi=6
glo_midu=0.1
x,y=sawtooth_wave(start=(z-1)*zhouqi,zhouqi=zhouqi,midu=glo_midu,xdecimals=2,ydecimals=5)

j=0
for i in range(zongshu):
    time.sleep(0.000001)

    print('we are saving')
    sql = "INSERT INTO  v_data_monitor(subsys_id,register_id,exp_id,v_data,v_data_time) values (5,1,2,%f,NOW(6));" % (y[j])
    cur.execute(sql)
    db.commit()
    j = j + 1
    # i = i + 1
    if j>=zhouqi/glo_midu:
        j=0
        z= z + 1
        print('z的大小',z)
        x, y = sawtooth_wave(start=(z-1)*zhouqi, zhouqi=zhouqi, midu=glo_midu, xdecimals=2, ydecimals=5)
