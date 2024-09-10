def last_digit_fibonacci(n):
    period = 60
    n = n % period
    
    if n == 0:
        return 0
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
    
    return b

n = int(input())
print(last_digit_fibonacci(n))
