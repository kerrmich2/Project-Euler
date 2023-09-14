from factors import factors

def phi(n):
    relatively_prime = []
    for i in range(1, n):
        items = factors(i)
        del items[0]
        not_relatively_prime = True
        for element in items:
            if element in factors(n):
                not_relatively_prime = False
        if not_relatively_prime:
            relatively_prime.append(i)
    if n == 1:
        relatively_prime.append(1)
    return len(relatively_prime)

def f(x):
    return x/phi(x)

f_list = []
for i in range(1, 1000):
    f_list.append(f(i))
    print(i)

print(max(f_list))