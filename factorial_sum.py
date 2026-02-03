Ссылка на Задачу: [Сумма факториалов!](https://stepik.org/lesson/298796/step/4?unit=280623)

# 1-ое решение с модулем Math

from math import factorial

print('Сумма факториалов ❗')

n = int(input())
total = 0

for i in range(1, n + 1):
    total += factorial(i)

print(total)

# 2-ое Решение c вложенными циклами

print('Сумма факториалов ❗')

n = int(input())

total = 0
count = 1
factorial = 1

for i in range(1, n + 1):
    for f in range(count, i + 1):
        factorial *= i
        count += 1
        
    total += factorial

print(total)
