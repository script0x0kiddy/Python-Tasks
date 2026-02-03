Ссылка на задачу: https://stepik.org/lesson/298796/step/5?unit=280623

print('Подставь и узнаешь 💡')

n = int(input())
m = int(input())

rebus = 1
checker = False

for i in range(1, n):
    for j in range(1, n):
        for z in range(1, n):
            if (i + 3 * j + 2 * z) == m:
                checker = True
                print(f"{i} + 3×{j} + 2×{z} = {m}")

if checker == False:
    print('При заданных n и m решений не существует.')
