
import pymysql
import numpy as np




# database connect
db = pymysql.connect(host='localhost', user='root', password='123456', db='test', port=3306, charset='utf8')
cur = db.cursor()

import time

start_time = time.process_time()

Z=1
x = np.arange((Z - 1) * 2 * np.pi, 2 * np.pi, 0.000001)

y = np.sin(x) * 100
j=0
for i in range(100000):
    time.sleep(0.000001)

    print('we are saving')
    sql = "INSERT INTO sinvalue (xval,yval) values (%f,%f);" % (x[j], y[j])
    cur.execute(sql)
    db.commit()
    j = j + 1

    if j==63:
        print('we are in here')
        j=0
        Z= Z + 1
        x = np.arange((Z - 1) * 2 * np.pi, (Z - 1) * 2 * np.pi+2 * np.pi, 0.0000001)
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