# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
from is_prime import first_n_primes
import itertools

def permutations(n):
    return list(itertools.permutations(n))

# Also remove all leading zeroes.
def combine_into_string(n):
    # Convert to string, then join.
    string_join = [''.join([str(j) for j in i]) for i in n]
    count = 0
    for i in string_join:
        if i[0] == '0':
            string_join[count] = None
        count += 1

    string_join_non_zero = [i for i in string_join if i is not None]

    # There should be n! - n!/n = (n-1)!(n-1) elements.
    return string_join_non_zero

def remove_all_leading_zeroes_in_list(n):
    count = 0
    for i in n:
        if str(i[0]) == str(0):
            n[count] = None
        count += 1

    non_zero = [i for i in n if i is not None]

    return non_zero

def three_string_rotations(n):
    rotations = []

    for i in range(0, len(n)):
        if i+2 > len(n)-1:
            break
        rotations.append([n[i], n[i+1], n[i+2]])

    rotations_join = [''.join(i) for i in rotations]

    return rotations_join

def main():
    perm = permutations([i for i in range(0, 4)])
    string_join = [''.join([str(j) for j in i]) for i in perm]
    perm_0 = remove_all_leading_zeroes_in_list(string_join)
    count = 0
    substring_divisible_numbers = []
    for i in perm_0:
        count += 1
        print(count)
        tsr = [int(i) for i in three_string_rotations(i)]
        tsr.pop(0)
        true = True
        for j in range(0, len(tsr) + 1):
            if tsr[j] % first_n_primes(len(tsr))[j] != 0:
                true = False
                break
        if true:
            substring_divisible_numbers.append(i)

if __name__ == "__main__":
    main()


































