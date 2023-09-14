def is_palindromic(z):
    if list(str(z)) == list(str(z))[::-1]:
        return True
    else:
        return False

count = 0

for i in range(1, 1000001):
    if is_palindromic(i) and is_palindromic(bin(i)[2:]):
        count += i

print(count)