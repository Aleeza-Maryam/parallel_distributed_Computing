import threading

TOTAL_NUMBERS = 1000000
NUM_THREADS = 4

results = [0] * NUM_THREADS

def calculate_sum(start, end, index):
    s = 0
    for i in range(start, end + 1):
        s += i
    results[index] = s

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

final_sum = sum(results)

print("Final Sum:", final_sum)