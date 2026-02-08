print('Делители-2 🌶️')

a = int(input())
b = int(input())
total_delitel = 0 # Сумма всех делителей числа _k_
max_num = 0 # Число с максимальной суммой делителей
variable = 0 # Сумма всех делителей из числа max_num

for i in range(a, b + 1):
    total_delitel = 0
    
    for k in range(1, i + 1):
        if i // k >= 1 and i % k == 0:
            total_delitel += k
            
            if total_delitel > variable:
                variable = total_delitel
                max_num = k

            elif total_delitel == variable:
                max_num = k

print(max_num, variable)
