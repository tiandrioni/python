big_list = [0, True, 2.0, [3, ], (4, ), {5}, '6', {7: 8}]

for element in big_list:
	el_type = str(type(element)).split("'")[1]
	print(f'Элемент {element} имеет тип {el_type}.')

input()