# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 1
b = 1
for a in range(1, 1001):
    for b in range(1, 1001):
        if ((a**2 + b**2)**(1/2)).is_integer():
            c = (a**2 + b**2)**(1/2)
            if a + b + c == 1000:
                print(a*b*c)
        b += 1
    a += 1