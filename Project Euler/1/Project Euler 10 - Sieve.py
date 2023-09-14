from sieve import sieve
import time


def project_10(n):
    return sum(sieve(n))


t0 = time.time()
print(project_10(10000))
t1 = time.time()

total = t1-t0
print(total)
