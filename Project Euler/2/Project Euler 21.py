# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from functools import reduce

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def d(n):
    return sum(factors(n))-n

def f(n):
    x = d(n)
    if d(n) == n:
        return False
    elif d(x) == n:
        return True
    else:
        return False

x = set()
for i in range(2, 10001):
    if f(i):
        x.add(i)
        x.add(d(i))
print(sum(x))