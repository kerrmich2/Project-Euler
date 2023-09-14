# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

import math
# I used the 40c20 formula
print(math.factorial(40)/(math.factorial(20)*(math.factorial(40-20))))