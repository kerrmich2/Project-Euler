# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

number = ""
for i in range(0, 10):
    number += str(sum([i**i for i in range(1, 1001)]))[::-1][i]
print(number[::-1])