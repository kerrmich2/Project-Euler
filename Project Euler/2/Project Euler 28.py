# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def diagonals(n, num_list):
    x = n**2
    for i in range(0, 4):
        x -= (n-1)
        num_list.append(x)
    return num_list

number_sum = []

for i in range(1, 501):
    number_sum.append(diagonals((2*i + 1), []))

flat_list = [i for sublist in number_sum for i in sublist]

flat_list.sort()

print(sum(flat_list)+(1001**2)) # My spiral doesn't include the very last corner, therefore I have to manually add it in