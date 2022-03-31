import time

input('Press enter to start')

start_time = time.perf_counter()
for i in range(10000000):
    x = i * i
end_time = time.perf_counter()

print(end_time - start_time)

