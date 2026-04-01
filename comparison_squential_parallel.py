import threading
import time

TOTAL_NUMBERS = 1000000
NUM_THREADS = 4
results = [0] * NUM_THREADS

def calculate_sum(start, end, index):
    s = 0
    for i in range(start, end + 1):
        s += i
    results[index] = s


# Sequential Execution
start_time = time.time()

seq_sum = 0
for i in range(1, TOTAL_NUMBERS + 1):
    seq_sum += i

seq_time = time.time() - start_time

print("Sequential Sum:", seq_sum)
print("Sequential Time:", seq_time)


# Multithreaded Execution
start_time = time.time()

threads = []
range_size = TOTAL_NUMBERS // NUM_THREADS

for i in range(NUM_THREADS):
    start = i * range_size + 1
    end = (i + 1) * range_size

    t = threading.Thread(target=calculate_sum, args=(start, end, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

parallel_sum = sum(results)
parallel_time = time.time() - start_time

print("Multithreading Sum:", parallel_sum)
print("Multithreading Time:", parallel_time)