print('Самый частотный символ')

# -------------------------------

# Метод решения №1

string = str(input())
max_sim = ""
now_a = string[0]
count = 0
max_copy = 0

for k in range(0, len(string)):
	if now_a == string[k]:
		count += 1

		if count >= max_copy:
			max_copy = count
			max_sim = string[k]

	elif now_a != string[k]:
		count = 1
		now_a = string[k]

print(max_sim)

# --------------------------------

# Метод решения №2

string = str(input())
max_sim = ''
max_copy = 0

for i in range(0, len(string)):
    if string.count(string[i]) >= max_copy:
        max_copy = string.count(string[i])
        max_sim = string[i]
        
print(max_sim)
