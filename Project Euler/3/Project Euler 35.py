# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from is_prime import is_prime

def prime_num(z):
    rotations = []
    permutation = ''
    digits = [int(i) for i in list(str(z))]

    for i in digits:
        digits.append(digits[0])
        del digits[0]
        rotations += digits

    for i in range(1, len(rotations)+1):
        permutation += str(rotations[i-1])

    permut = [permutation[i:i+len(digits)] for i in range(0, len(permutation), len(digits))]
    permut = [int(i) for i in permut]

    for i in permut:
        if not is_prime(i):
            return False

    return True

count = 0

for i in range(1, 1000001):
    if prime_num(i):
        count += 1

print(count)