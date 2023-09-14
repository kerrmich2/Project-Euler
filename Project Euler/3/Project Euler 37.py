# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
from is_prime import is_prime

def is_truncatable(z):
    # Left to right:
    prime = list(str((z)))
    prime_num = z
    if not is_prime(prime_num):
        return False
    for i in range(1, len(prime)+1):
        if not is_prime(prime_num):
            return False
        del prime[0]
        print(''.join(prime), z)
    return z

for i in range(1, 100):
    if not is_truncatable(i) == False:
        print(is_truncatable(i))