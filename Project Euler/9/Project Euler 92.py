def chain(x):
    if x == 1:
        return False
    if x == 89:
        return True
    return chain(sum([i**2 for i in [int(i) for i in str(x)]]))

count = 0

for i in range(1, 10000001):
    if chain(i):
        count += 1
print(count)