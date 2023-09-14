# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math
from is_prime import is_prime

count = 0
i = 0
while True:
    if is_prime(i):
        count += 1
    if count == 10001:
        print(i)
        break
    i += 1