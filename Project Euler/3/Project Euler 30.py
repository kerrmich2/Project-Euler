# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import math

count = 1
nines = 9**5

while True:
    if math.log10(count).is_integer():
        nines += 9**5
    if count > nines:
        upper_limit = count
        break
    count += 1

summy = 0

for i in range(1, upper_limit):
    characters = [int(z) for z in list(str(i))]
    if sum([j**5 for j in characters]) == i:
        print(characters, i)
        summy += i
print(summy-1)