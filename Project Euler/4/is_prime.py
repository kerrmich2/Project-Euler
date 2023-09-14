import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def first_n_primes(n):
    count = 0
    k = 1
    prime_list = []
    while True:
        if n == count:
            return prime_list
        if is_prime(k):
            count += 1
            prime_list.append(k)
        k += 1

