# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import math
from is_prime import is_prime

def long_division(divisor, dividend, num_list, dividend_list):
    if dividend % divisor == 0:
        return len(num_list)
    if math.floor(dividend/divisor) == 0:
        return long_division(divisor, dividend*10, num_list, dividend_list)
    num_list.append(math.floor(dividend/float(divisor)))
    dividend = dividend % divisor
    if dividend in dividend_list:
        return num_list
    else:
        dividend_list.append(dividend)
    return long_division(divisor, dividend, num_list, dividend_list)


