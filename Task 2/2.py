a = int(input())
b = int(input())
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    result = a + b**2
    print("a + b**2 = " + str(a+b**2))
else:
    print("Ошибка: числа должны быть в диапазоне от -10^9 до 10^9.")



