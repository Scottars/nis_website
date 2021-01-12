import time

import epics
import pymysql

pv = epics.PV('scottar:voltage:ai')
# conn = pymysql.connect(host='192.168.127.200', port=3306, user='root', passwd='wangsai', db='nis_hsdd', charset='utf8')
# cur = conn.cursor()

# 遍历pv,获取pv中的值
for i in range(1000):
    a=pv.value
    print('PV_Value 第',i,'次 is:',a)

    sql = "insert into test_table(voltage) values(%f)" %(a)
    # 执行SQL, new_list是执行参数, 用于替换上面SQL中的占位符%s,%s,%s
    # cur.execute(sql)
    # conn.commit()
    time.sleep(1)
