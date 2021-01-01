starting_list = input('Введите элементы списка через пробел: ').split()
print(starting_list)
final_list = starting_list
for index in range(len(final_list) // 2):
	a = final_list[2*index + 1]
	b = final_list[2*index]
	final_list[2*index + 1] = b
	final_list[2*index] = a

print(final_list)

input()