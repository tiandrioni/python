words = input('Введите слова через пробел: ').split()

for index in range(len(words)):
	word = words[index]
	if len(word) > 10:
		word = word[:10] + '...'
	print(f'{index + 1} - {word}')

input()