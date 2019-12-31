
import pymysql
import numpy as np




# database connect
db = pymysql.connect(host='localhost', user='root', password='123456', db='nis_hsdd', port=3306, charset='utf8')
cur = db.cursor()

import time

start_time = time.process_time()

Z=1
x = np.arange((Z - 1) * 2 * np.pi, 2 * np.pi, 0.1)

y = np.sin(x) * 100
j=0
for i in range(1000):
    time.sleep(0.000001)

    print('we are saving')
    sql = "INSERT INTO  v_data_monitor(subsys_id,register_id,exp_id,v_data,v_data_time) values (5,1,1,%f,NOW(6));" % (y[j])
    cur.execute(sql)
    db.commit()
    j = j + 1

    if j==63:
        print('we are in here')
        j=0
        Z= Z + 1
        x = np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi+2 * np.pi, 0.1)
        y = np.sin(x) * 100



# sql = "INSERT INTO test (time,username,tweet) values ('2','2','2');"
# cur.execute(sql)
#
# sql = "INSERT INTO test (time,username,tweet) values ('3','3','3');"
# cur.execute(sql)
#
# sql = "INSERT INTO test (time,username,tweet) values ('4','4','4');"
# cur.execute(sql)
end_time = time.process_time()
print(end_time-start_time)
# print(b[2])