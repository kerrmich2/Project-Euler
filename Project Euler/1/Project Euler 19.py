# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

day = 2
count = 0
for j in range(1901, 2001):
    for i in range(1, 13):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            day += 31 % 7
        elif i == 4 or i == 6 or i == 9 or i == 1:
            day += 30 % 7
        else:
            if j % 4 == 0:
                day += 29 % 7
            else:
                day += 28 % 7
        day = day % 7
        if day == 0:
            count += 1

print(count)