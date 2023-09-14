# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

for i in range(1, 101):
    for j in range(1, 101):
        list_i = list(str(i))
        list_j = list(str(j))
        if (i / j) > 1:
            continue
        if ("0" in list_j) or ("0" in list_i):
            continue
        for k in list_i:
            if k in list_j:
                list_j.remove(str(k))
                list_i.remove(str(k))
                print(list_i, list_j)