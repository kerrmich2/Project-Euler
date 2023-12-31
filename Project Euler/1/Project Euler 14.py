# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def f(x, count):
    if x == 1:
        return count
    if x % 2 == 0:
        x *= 0.5
    else:
        x = (3*x) + 1
    count += 1
    return f(x, count)

big_count = 0
big_num = 0
for i in range(1, 1000001):
    if f(i, 0) > big_count:
        big_count = f(i, 0)
        big_num = i
    if i % 100 == 0:
        print(i)
print(big_num)