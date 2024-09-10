a = int(input())
b = int(input())
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    print("a + b = " + str (a+b))
else:
    print("Ошибка: числа должны быть в диапазоне от -10^9 до 10^9.")

