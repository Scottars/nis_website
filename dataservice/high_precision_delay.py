import time


print(time.perf_counter())

def high_precision_delay(delay_time):
    _ = time.perf_counter_ns() + delay_time*1000000000
    while time.perf_counter_ns() < _:
        pass



start_time = time.process_time()
high_precision_delay(1)
end_time = time.process_time()
print('延时1s',end_time-start_time)

start_time = time.perf_counter()
high_precision_delay(0.1)
end_time = time.perf_counter()
print('延时0.1s',end_time-start_time)

start_time = time.perf_counter()
high_precision_delay(0.01)
end_time = time.perf_counter()
print('延时0.01s',end_time-start_time)

start_time = time.perf_counter()
high_precision_delay(0.001)
end_time = time.perf_counter()
print('延时0.001s',end_time-start_time)

start_time = time.perf_counter()
high_precision_delay(0.0001)
end_time = time.perf_counter()
print('延时0.0001s',end_time-start_time)

start_time = time.perf_counter()
high_precision_delay(0.00001)
end_time = time.perf_counter()
print('延时0.00001s',end_time-start_time)

start_time = time.perf_counter()
high_precision_delay(0.000001)
end_time = time.perf_counter()
print('延时0.000001s',end_time-start_time)


start_time = time.perf_counter()
high_precision_delay(0.0000001)
end_time = time.perf_counter()
print('延时0.0000001s',end_time-start_time)
