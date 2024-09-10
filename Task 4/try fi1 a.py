from memory_profiler import memory_usage
import time

def calc_fib(n):
    if n <= 1:
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)

def measure_memory_usage():
    start_time = time.time()
    mem_usage = memory_usage((calc_fib, (n,)))
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")
    print(f"Используемая память: {max(mem_usage) - min(mem_usage)} МБ")

if __name__ == '__main__':
    n = int(input("F(n): "))
    print(calc_fib(n))
    measure_memory_usage()
