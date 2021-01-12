import time

import epics
import pymysql

# 定义类
PV = epics.PV('scottar:voltage:ai')

'''PV 若是不在线，则报如下错误：
Failed to start executable - "caRepeater". ϵͳ�Ҳ���ָ�����ļ���

Changes may be required in your "path" environment variable.
caStartRepeaterIfNotInstalled (): unable to start CA repeater daemon detached process
CA client library is unable to contact CA repeater after 50 tries.
Silence this message by starting a CA repeater daemon
or by calling ca_pend_event() and or ca_poll() more often.
'''


''' 供气系统 '''

GAS_PUFF_TRIG_MODE = epics.PV('GF:GAS_PUFF_TRIG_MODE')
GAS_PUFF_ON_OFF = epics.PV('GF:GAS_PUFF_ON_OFF')
GAS_FLOW_SET = epics.PV('GF:GAS_FLOW_SET')
GAS_FLOW_PUFF_SET = epics.PV('GF:GAS_FLOW_PUFF_SET')
DRIVER_PRESS_SET = epics.PV('GF:DRIVER_PRESS_SET')
GAS_PEV_PUFF_SET = epics.PV('GF:GAS_PEV_PUFF_SET')
PID_P_SET = epics.PV('GF:PID_P_SET')
PID_I_SET = epics.PV('GF:PID_I_SET')
PID_D_SET = epics.PV('GF:PID_D_SET')
PEV_VAL_SET = epics.PV('GF:PEV_VAL_SET')
GF_1 =  epics.PV('GF:1')
GF_2 =  epics.PV('GF:2')
GF_3 =  epics.PV('GF:3')
GF_4 =  epics.PV('GF:4')
GF_5 =  epics.PV('GF:5')
GF_6 =  epics.PV('GF:6')
GF_7 =  epics.PV('GF:7')
GF_8 =  epics.PV('GF:8')
GF_9 =  epics.PV('GF:9')
GF_10 =  epics.PV('GF:10')
GF_11 =  epics.PV('GF:11')
GF_12 =  epics.PV('GF:12')
GF_13 =  epics.PV('GF:13')
GF_14 =  epics.PV('GF:14')
GF_15 =  epics.PV('GF:15')
GF_16 =  epics.PV('GF:16')

'''射频系统'''

RF_FIX_POW_SET = epics.PV('RF:FIX_POW_SET')

'''PG 电源'''
PG_VOL_SET = epics.PV('PG_VOL_SET')
PG_CUR_SET = epics.PV('PG_CUR_SET')

'''引出电源'''
EXT_VOL_SET = epics.PV('EXTR:VOL_SET')
EXT_CUR_SET = epics.PV('EXTR:CUR_SET')

'''加速电源'''
# ACCE_MAX_SET = epics.PV('ACCE:MAX_SET')
# ACCE_MIN_SET = epics.PV('ACCE:MIN_SET')

'''腔体偏压电源'''
CHAMBER_BIAS_VOL_SET = epics.PV('CHAMBER_BIAS:VOL_SET')

'''时序控制系统'''
TIMING_STR_SET1 = epics.PV('TIMING_STR_SET1')
TIMING_STR_SET2 = epics.PV('TIMING_STR_SET2')
TIMING_STR_SET3 = epics.PV('TIMING_STR_SET3')
TIMING_STR_SET4 = epics.PV('TIMING_STR_SET4')
TIMING_STR_SET5 = epics.PV('TIMING_STR_SET5')
TIMING_STR_SET6 = epics.PV('TIMING_STR_SET6')
TIMING_STR_SET7 = epics.PV('TIMING_STR_SET7')
TIMING_STR_SET8 = epics.PV('TIMING_STR_SET8')
TIMING_STR_SET9 = epics.PV('TIMING_STR_SET9')
TIMING_STR_SET10 = epics.PV('TIMING_STR_SET10')
TIMING_STR_SET11 = epics.PV('TIMING_STR_SET11')
TIMING_STR_SET12 = epics.PV('TIMING_STR_SET12')
TIMING_STR_SET13 = epics.PV('TIMING_STR_SET13')
TIMING_STR_SET14 = epics.PV('TIMING_STR_SET14')
TIMING_STR_SET15 = epics.PV('TIMING_STR_SET15')
TIMING_STR_SET16 = epics.PV('TIMING_STR_SET16')

TIMING_END_SET1 = epics.PV('TIMING_END_SET1')
TIMING_END_SET2 = epics.PV('TIMING_END_SET2')
TIMING_END_SET3 = epics.PV('TIMING_END_SET3')
TIMING_END_SET4 = epics.PV('TIMING_END_SET4')
TIMING_END_SET5 = epics.PV('TIMING_END_SET5')
TIMING_END_SET6 = epics.PV('TIMING_END_SET6')
TIMING_END_SET7 = epics.PV('TIMING_END_SET7')
TIMING_END_SET8 = epics.PV('TIMING_END_SET8')
TIMING_END_SET9 = epics.PV('TIMING_END_SET9')
TIMING_END_SET10 = epics.PV('TIMING_END_SET10')
TIMING_END_SET11 = epics.PV('TIMING_END_SET11')
TIMING_END_SET12 = epics.PV('TIMING_END_SET12')
TIMING_END_SET13 = epics.PV('TIMING_END_SET13')
TIMING_END_SET14 = epics.PV('TIMING_END_SET14')
TIMING_END_SET15 = epics.PV('TIMING_END_SET15')
TIMING_END_SET16 = epics.PV('TIMING_END_SET16')


'''灯丝偏压'''
BIAS_VOL_SET = epics.PV('BIAS_VOL_SET')
BIAS_CUR_SET = epics.PV('BIAS_CUR_SET')

'''灯丝加热'''
HEAT_VOL_SET = epics.PV('HEAT_VOL_SET')
HEAT_CUR_SET = epics.PV('HEAT_CUR_SET')

'''连接数据库'''
# conn = pymysql.connect(host='192.168.127.200', port=3306, user='root', passwd='wangsai', db='nis_hsdd', charset='utf8')
# cur = conn.cursor()
# 遍历PV,获取PV中的值


PVS = [GAS_PUFF_TRIG_MODE,GAS_PUFF_ON_OFF,GAS_FLOW_SET,GAS_FLOW_PUFF_SET,DRIVER_PRESS_SET,GAS_PEV_PUFF_SET,PID_P_SET,PID_I_SET,PID_D_SET,PEV_VAL_SET
        ,GF_1,GF_2,GF_3,GF_4,GF_5,GF_6,GF_7,GF_8,GF_9,GF_10,GF_11,GF_12,GF_13,GF_14,GF_15,GF_16
        ,RF_FIX_POW_SET
       ,PG_VOL_SET,PG_CUR_SET
       ,EXT_VOL_SET,EXT_CUR_SET
       ,CHAMBER_BIAS_VOL_SET
       ,TIMING_STR_SET1,TIMING_STR_SET2,TIMING_STR_SET3,TIMING_STR_SET4,TIMING_STR_SET5,TIMING_STR_SET6,TIMING_STR_SET7,TIMING_STR_SET8,TIMING_STR_SET9,TIMING_STR_SET10,TIMING_STR_SET11,TIMING_STR_SET12,TIMING_STR_SET13,TIMING_STR_SET14,TIMING_STR_SET15,TIMING_STR_SET16
        ,TIMING_END_SET1,TIMING_END_SET2,TIMING_END_SET3,TIMING_END_SET4,TIMING_END_SET5,TIMING_END_SET6,TIMING_END_SET7,TIMING_END_SET8,TIMING_END_SET9,TIMING_END_SET10,TIMING_END_SET11,TIMING_END_SET12,TIMING_END_SET13,TIMING_END_SET14,TIMING_END_SET15,TIMING_END_SET16
       ]
# 数据库存储，如果存储为None 则表示该EPICS 并不在线
for i in range(len(PVS)):
    print(str(PVS[i].pvname),':', PVS[i].value)


    # sql = "insert into test_table(GAS_PUFF_TRIG_MODE.GAS_PUFF_ON_OFF) " \
    #       "values(%f)" \
    #       %(10)
    # 执行SQL, new_list是执行参数, 用于替换上面SQL中的占位符%s,%s,%s
    # cur.execute(sql)
    # conn.commit()
    # time.sleep(1)
