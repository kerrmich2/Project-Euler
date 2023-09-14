# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math

def is_prime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def project_3(x):
    numlist = []
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            if is_prime(i):
                numlist.append(i)
            if is_prime(x/i):
                numlist.append(x/i)
        i += 1
    numlist.sort()
    if len(numlist) == 0:
        return None
    return numlist[len(numlist)-1]


print(project_3(6859430))