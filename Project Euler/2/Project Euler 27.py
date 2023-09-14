# Euler discovered the remarkable quadratic formula:
#
#       n2+n+41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
#       n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
from is_prime import is_prime

def f(a, b, count):
    while True:
        if not is_prime(count**2 + a*count + b):
            return count
        else:
            count += 1
            return f(a, b, count)

ZERO = 0
largest_sequence_product = 0
largest_sequence = 0

for i in range(-1000, 1000):
    for j in range(-1000, 1001):
        if f(i, j, ZERO) > largest_sequence:
            print(f(i, j, ZERO), (i, j))
            largest_sequence_product = i*j
            largest_sequence = f(i, j, ZERO)

print(largest_sequence_product)
