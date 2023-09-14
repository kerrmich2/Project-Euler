import math

def factors(n):
    factors_list = []
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            factors_list.append(i)
            factors_list.append(n/i)
    factors_list = list(set(factors_list))
    factors_list.sort()
    return factors_list

