'''
目标：对实时显示模块的参数的的配置
配置：zmq的连接的地址/UI刷新速度/

实现方式：
总计设定三个图像
（1） 最近1w个数据的实时显示
（2）数据累计的显示
（3）散点图显示
'''

# 基本设计说明
# req地址采用80xx  level 2 此处，同样是第二层的各个守护线程主动连接我们管理中心的线程
# req地址采用90xx level 3  此处，各个守护线程是实现主动去连接我们的管理中心的线程
# sub 地址采用50xx开始    此处，我们的实时显示模块管理中心想要获取，都是同样需要的是


level_2_02watercool_sub_addr = 'tcp://192.168.1.104:5002'
level_2_02_watercool_req_addr = 'tcp://192.168.1.8:8002'
level_3_02_watercool_req_addr = 'tcp://192.168.1.8:9002'
watercool_ui_intertal='10' #单位是ms


level_2_11_leadintoutpower_sub_addr = 'tcp://192.168.1.104:5011'
level_2_11_leadintoutpower_req_addr = 'tcp://192.168.1.8:8011'
level_3_11_leadingoutpower_req_addr = 'tcp://192.168.1.8:9011'
leadingoutpower_ui_intertal='10' #单位是ms


level_3_para_read_req_addr  = 'tcp://192.168.1.8:10011'
