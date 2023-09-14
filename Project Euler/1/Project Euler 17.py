# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

num_words = {0: '', 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
             10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
             17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
             60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}

words = []
for i in range(1, 1000):
    if 1 <= i <= 19:
        words.append(num_words[i])
    if 20 <= i <= 99:
        x, y = divmod(i, 10)
        word = str(num_words[x*10])+str(num_words[y])
        words.append(word)
    if 100 <= i <= 999:
        hundred, ten2 = divmod(i, 100)
        ten, one = divmod(ten2, 10)
        word = str(num_words[hundred]) + "hundred"
        if not ten2 == 0:
            if 1 <= ten2 <= 19:
                word += "and" + str(num_words[ten2])
            else:
                word += "and" + str(num_words[ten*10]) + str(num_words[one])
        words.append(word)
words.append("Onethousand")
listy = []
for i in words:
    x = [listy.append(word) for word in i]
print(len(listy))