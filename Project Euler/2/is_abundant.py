from is_prime import is_prime
import math

def is_abundant(n):
    num_list = []
    if is_prime(n):
        return False
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            num_list.append(i)
            num_list.append(n/i)
        i += 1
    num_list.remove(n)
    num_list = set(num_list)
    if sum(num_list) > n:
        return True
    else:
        return False