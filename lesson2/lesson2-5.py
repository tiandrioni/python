top_list = [10, 10, 7, 6, 5, 5, 4]
rating = int(input('Введите рейтинг (целое число):'))
top_list.reverse()
print(top_list)
for i in range(len(top_list)):
	if rating < top_list[i]:
		top_list = top_list[:i] + [rating] + top_list[i:]
		break
if rating > top_list[-1]:
	top_list.append(rating)
top_list.reverse()
print(top_list)

input()