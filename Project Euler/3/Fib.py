def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1, 35):
    print(fib(i), i)