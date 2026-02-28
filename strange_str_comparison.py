# Cсылка на задачу: https://stepik.org/lesson/1402735/step/13?unit=1419697

print("Необычное сравнение 📊")

s1 = str(input()).lower()
s2 = str(input()).lower()

new_str = ""
new_str2 = ""

for i in s1:
    if i.isalpha():
        new_str += i

for k in s2:
    if k.isalpha():
        new_str2 += k

# РАБОТА ИСКЛЮЧИТЕЛЬНО С ЦИФРАМИ ДАЛЬШЕ

if new_str == "" and new_str2 == "":
    for z in s1:
        if z.isdigit():
            new_str += z

    for j in s2:
        if j.isdigit():
            new_str2 += j


checker = False

if len(new_str) > len(new_str2) or len(new_str) < len(new_str2):
    if new_str.isdigit() and new_str2.isdigit():
        short_word = new_str
        if len(new_str) > len(new_str2):
            short_word = new_str2
        elif len(new_str) < len(new_str2):
            short_word = new_str

        for i in range(0, len(short_word)):
            if new_str[i] == new_str2[i]:
                checker = True
            else:
                checker = True
                break

# КОНЕЦ РАБОТЫ С ЦИФРАМИ. ДАЛЬШЕ ТОЛЬКО СТРОКИ

elif len(new_str) == len(new_str2):
    for k in range(0, len(new_str)):
        if new_str[k] == new_str2[k]:
            checker = True
        else:
            checker = False
            break



if checker == True:
    print("YES")
else:
    print("NO")


print(new_str)
print(new_str2)
