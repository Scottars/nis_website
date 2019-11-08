import time


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

