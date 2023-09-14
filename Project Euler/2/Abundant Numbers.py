from is_abundant import is_abundant

with open("abundant numbers.txt", "w") as f:
    for i in range(1, 50001):
        if is_abundant(i):
            f.write(str(i) + "\n")