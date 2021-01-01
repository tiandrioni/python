products = []
product_name = input('Название товара: ')
number = 1
while product_name != '':
	product_dict = {'название': product_name}
	price = int(input('Цена товара: '))
	product_dict['цена'] = price
	quantity = int(input('Количество товара: '))
	product_dict['количество'] = quantity
	unit = input('Единица измерния: ')
	product_dict['ед'] = unit
	products += [(number, product_dict.copy())]
	number += 1
	print('-'*30)
	product_name = input('Название товара: ')
	
print(products)

analytics = {'название': [], 'цена': [], 
			 'количество': [], 'ед': []}

for product in products:
	for characteristic in analytics.keys():
		analytics[characteristic].append(product[1][characteristic])

print(analytics)
input()