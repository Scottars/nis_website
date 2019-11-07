
import pymysql


# database connect
db = pymysql.connect(host='localhost', user='root', password='123456', db='test', port=3306, charset='utf8')
cur = db.cursor()


sql = "INSERT INTO test (time,username,tweet) values ('hha','gga','adsf');"
cur.execute(sql)

sql = "INSERT INTO test (time,username,tweet) values ('2','2','2');"
cur.execute(sql)

sql = "INSERT INTO test (time,username,tweet) values ('3','3','3');"
cur.execute(sql)

sql = "INSERT INTO test (time,username,tweet) values ('4','4','4');"
cur.execute(sql)



# data = bytesToFloat(b[4], b[5], b[6], b[7])
# sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (5,%d,1,%f,NOW(6));" % (
# b[2], data)
# cur.execute(sql)
db.commit()
# print(b[2])