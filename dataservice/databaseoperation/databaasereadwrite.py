
import pymysql


'''
    关于计时程序运行的快慢的问题：
    方法1：datetime.datetime.now()
    方法2：time.time()
    方法3：time.clock()  
通过对以上方法的比较我们发现，方法二的精度比较高。方法一基本上是性能最差的。这个其实是和系统有关系的。一般我们推荐使用方法二和方法三。我
的系统是Ubuntu，也就是Linux系统，方法二返回的是UTC时间。 在很多系统中time.time()的精度都是非常低的，包括windows。

python 的标准库手册推荐在任何情况下尽量使用time.clock().但是这个函数在windows下返回的是真实时间（wall time）

方法一和方法二都包含了其他程序使用CPU的时间。方法三只计算了程序运行CPU的时间。

方法二和方法三都返回的是浮点数

'''

# database connect
db = pymysql.connect(host='localhost', user='root', password='123456', db='test', port=3306, charset='utf8')
cur = db.cursor()

import time

start_time = time.process_time()

for i in range(10000):
    sql = "INSERT INTO test (time,username,tweet) values ('hha','gga','adsf');"
    cur.execute(sql)

# sql = "INSERT INTO test (time,username,tweet) values ('2','2','2');"
# cur.execute(sql)
#
# sql = "INSERT INTO test (time,username,tweet) values ('3','3','3');"
# cur.execute(sql)
#
# sql = "INSERT INTO test (time,username,tweet) values ('4','4','4');"
# cur.execute(sql)
db.commit()
end_time = time.process_time()
print(end_time-start_time)
# print(b[2])