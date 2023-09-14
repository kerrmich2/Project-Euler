# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether!
# If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def num_list(fname):
    number_list = []
    with open(fname) as f:
        for i in range(file_len(fname)):
            text = f.readline().split()
            text = [int(i) for i in text]
            number_list.append(text)
    return number_list

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

file = "Triangle2.txt"

rows = file_len(file)
num_list = num_list(file)


for i in range(1, rows+1):
    j = 0
    while j < rows-i:
        num_list[rows-i-1][j] += maximum(num_list[rows-i][j], num_list[rows-i][j+1])
        j += 1

print(num_list[0][0])