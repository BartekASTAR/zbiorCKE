import string

with open("slowa.txt", "r") as f:
    file = [line.strip() for line in f.readlines()]

print(file)

letters = string.ascii_lowercase
print(letters)

ans = open("wyniki3.txt", "w")

#3.1
counter = 0
for i in file:
    for j in range(2, len(i)):
        if i[j-2] == "k" and i[j-1] in letters and i[j] == "t":
            counter += 1
            break
ans.write(f"3.1\n{counter}\n\n")

#3.2
def rot13(word):
    new_word = ""
    for i in word:
        if ord(i) + 13 > 122:
            letter = chr(ord(i) + 13 - 26)
        else:
            letter = chr(ord(i) + 13)
        new_word+=letter
    return new_word

counter = 0
longest = ""
for i in file:
    if i[::-1] == rot13(i):
        counter += 1
        if len(i) > len(longest):
            longest = i
ans.write(f"3.2\n{counter}\n{longest}\n\n")

#3.3
dicts = []
for i in file:
    temp_dict = {}
    for j in i:
        if j in temp_dict.keys():
            temp_dict[j] += 1
        else:
            temp_dict[j] = 1
    temp_dict["len"] = len(i)
    temp_dict["word"] = i
    dicts.append(temp_dict)

ans.write(f"3.3\n")

for i in dicts:
    for v in i.values():
        if v != i["len"] and v != i["word"] and v >= i["len"]/2:
            ans.write(f"{i["word"]}\n")
            break





