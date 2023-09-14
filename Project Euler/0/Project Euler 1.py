# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# My second attempt
z = 0
for i in range(1, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        z += i
print(z)

# List Comprehension Way
print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))

# My first attempt
mylist = []
i = 1
z = 3
while i <= 333:
    z = 3*i
    i += 1
    mylist.append(z)
i = 1
z = 5
while i <= 200:
    z = 5 * i
    i += 1
    mylist.append(z)
mylist = list(dict.fromkeys(mylist))
mylist.sort()
mylist.pop()
sum = sum(mylist)
print(sum)







