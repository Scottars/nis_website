import socket
import  struct
import pymysql
import time
def floatToBytes(f):
    bs = struct.pack("f",f)
    return (bs[3],bs[2],bs[1],bs[0])
def bytesToFloat(h1,h2,h3,h4):
    ba = bytearray()
    ba.append(h1)
    ba.append(h2)
    ba.append(h3)
    ba.append(h4)
    return struct.unpack("!f",ba)[0]
#
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('115.156.162.76',5000))

print('we have already connected')
#database connect
db=pymysql.connect(host='localhost',user='root',password='123456', db='nis_hsdd',port=3306,charset='utf8')
cur=db.cursor()

timebegin=time.process_time()
i=10000
while i>0:
        print('we are receiving data ')
        i=i-1
        b = s.recv(100)
        a=b.decode()
        # print(a)
        # print(type(a))
        c = int(a)
        # print(c)

        sql = "INSERT INTO test (test_data,data_time) values (%d ,NOW(6));" % (c)
        cur.execute(sql)

        db.commit()


timeend=time.process_time()
print('总计消耗时间：',timeend-timebegin)



