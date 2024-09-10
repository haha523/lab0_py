from memory_profiler import memory_usage
import time

def last_digit_fibonacci(n):
    period = 60
    n = n % period
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
    return b

def measure_memory_usage():
    start_time = time.time()
    mem_usage = memory_usage((last_digit_fibonacci, (n,)))
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")
    print(f"Используемая память: {max(mem_usage) - min(mem_usage)} МБ")

if __name__ == '__main__':
    n = int(input("F(n): "))
    print(last_digit_fibonacci(n))
    measure_memory_usage()
