# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from is_prime import is_prime

def project_10(n):
    z = 0
    for i in range(1, n):
        if is_prime(i):
            z += i
        print(i)
    return z

print(project_10(2000000))