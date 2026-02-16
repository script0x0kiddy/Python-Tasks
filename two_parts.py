print("Две половинки 🌶️")

from math import ceil

string = str(input())
left = ""
right = ""

if len(string) // 2 == 1:
    for i in range(0, len(string)):
        if i <= len(string) // 2:
            left = string[:i]
        if i >= len(string) // 2:
            right = string[i:]
            break

elif len(string) % 2 == 0:
    for i in range(0, len(string)):
        if i <= len(string) // 2:
            left = string[:i]
        elif i >= len(string) // 2:
            right = string[i - 1:]
            break

elif len(string) % 2 != 0:
    for i in range(0, len(string)):
        if i <= ceil(len(string) / 2):
            left = string[:i]
        elif i >= ceil(len(string) / 2):
            right = string[i - 1:]
            break

if left == "" and right == "":
    left = string
    print(left)
else:
    print(right, left, sep="")