import time

'''
    根据python 官方手册对process_time 以及perf_counter的定义：
    time.process_time() → float        
    Return the value (in fractional seconds) of the sum of the system and user CPU time of the current process. 
    It does not include time elapsed during sleep. It is process-wide by definition. 
    The reference point of the returned value is undefined, 
    so that only the difference between the results of consecutive calls is valid.
    
    time.perf_counter() → float
    Return the value (in fractional seconds) of a performance counter, 
    i.e. a clock with the highest available resolution to measure a short duration.
     It does include time elapsed during sleep and is system-wide. 
     The reference point of the returned value is undefined, 
     so that only the difference between the results of consecutive calls is valid.
'''


print('测试time.slepp 对 process_time,perfcount的关系的影响：')
start_time_process = time.process_time()
time.sleep(10)
end_time_process = time.process_time()
print('process_time:',end_time_process-start_time_process)
start_time_perf = time.perf_counter()
time.sleep(10)
end_time_perf = time.perf_counter()
print('perf_time:',end_time_perf-start_time_perf)



start_time = time.process_time()
time.sleep(1)
end_time = time.process_time()
print('延时1s',end_time-start_time)


start_time = time.perf_counter()
time.sleep(0.1)
end_time = time.perf_counter()
print('延时0.1s',end_time-start_time)

start_time = time.perf_counter()
time.sleep(0.01)
end_time = time.perf_counter()
print('延时0.01s',end_time-start_time)

start_time = time.perf_counter()
time.sleep(0.001)
end_time = time.perf_counter()
print('延时0.001s',end_time-start_time)

start_time = time.perf_counter()
time.sleep(0.0001)
end_time = time.perf_counter()
print('延时0.0001s',end_time-start_time)

start_time = time.perf_counter()
time.sleep(0.00001)
end_time = time.perf_counter()
print('延时0.00001s',end_time-start_time)

start_time = time.perf_counter()
time.sleep(0.000001)
end_time = time.perf_counter()
print('延时0.000001s',end_time-start_time)


start_time = time.perf_counter()
time.sleep(0.0000001)
end_time = time.perf_counter()
print('延时0.0000001s',end_time-start_time)

print('通过测试的结论，起最高的精度不超过10%的情况下：1000us')
print('通过测试的结论，起最高的精度不超过50%的情况下：100us')

