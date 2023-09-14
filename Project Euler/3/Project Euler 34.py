# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

count = 1
nines = 0

while True:
    if math.log10(count).is_integer():
        nines += math.factorial(9)
    if count > nines:
        upper_limit = count
        break
    count += 1

summy = 0

for i in range(1, upper_limit):
    int_list = [int(i) for i in list(str(i))]
    thicc_list = [math.factorial(i) for i in int_list]
    if sum(thicc_list) == i:
        summy += i
print(summy-3)