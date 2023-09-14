import math

def factors(n):
    factors = []
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n/i)
    factors = list(set(factors))
    factors.sort()
    return factors