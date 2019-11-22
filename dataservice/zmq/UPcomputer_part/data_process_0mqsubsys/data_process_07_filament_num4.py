'''
子系统自身信息：
IP:192.168.127.7
slave：05
port:5001

子系统需要检测的信息    如果这个子系统能够我不去询问，其能够 主动向上发送数据吗？ ----下面的内容还没有进行修改
加热电压监测 value1:data ----registerid=05   datatype=float
电源电流采样 value1:data --registerid=06   datatype=float
偏置电压监测 value1:data ----registerid=07   datatype=float   下面这两个位置不不确定
偏置电流监测 value1:data --registerid=08   datatype=float


额外说明：实际的电源中是不遵循modbus协议的，其是直接间数据上传到上位机
'''

