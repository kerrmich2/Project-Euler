# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

letters = []
names = []
count = 0
word = ""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name_list = []

with open("names.txt") as f:
    for i in f.read():
        letters.append(i)

for i in letters:
    if (count + 1) == len(letters):
        break
    if i == '"':
        while True:
            count += 1
            if letters[count] == '"':
                names.append(word)
                word = ''
                break
            prev_word = letters[count]
            word += prev_word

while ',' in names:
    names.remove(',')
names.sort()

for i in names:
    namescore = 0
    for j in i:
        namescore += (alphabet.index(j.lower())+1)
    name_list.append(namescore*(names.index(i)+1))

print(sum(name_list))