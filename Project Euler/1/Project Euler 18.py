# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

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

file = "Triangle1.txt"

rows = file_len(file)
num_list = num_list(file)


for i in range(1, rows+1):
    j = 0
    while j < rows-i:
        num_list[rows-i-1][j] += maximum(num_list[rows-i][j], num_list[rows-i][j+1])
        j += 1

print(num_list)