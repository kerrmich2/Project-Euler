# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(m):
    num_list = []
    reversed_list = []
    for i in str(m):
        num_list.append(i)
        reversed_list.append(i)
    reversed_list.reverse()
    if num_list == reversed_list:
        return True
    else:
        return False

biggest_number = 101
for i in range(1, 1000):
    for z in range(1, 1000):
        if is_palindrome(i*z) and biggest_number < i*z:
            biggest_number = i*z
print(biggest_number)