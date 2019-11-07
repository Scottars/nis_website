

import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

import time
r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379


start_time = time.clock()
for i in range(100000):
    r.set('name', i)  # key是"foo" value是"bar" 将键值对存入redis缓存

end_time = time.clock()


print('实际花费的时间',end_time-start_time)



