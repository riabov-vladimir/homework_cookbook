cook_book = {} # ключи - названия блюд, значения - списки из словарей с игредиентами


def ingredient(ing_line):
	'''Функция, которая принимает строку с ингридиентами и возвращает словарь'''
	ing_line = ing_line.split(' | ')
	a = {}
	a['ingredient_name'] = ing_line[0]
	a['quantity'] = ing_line[1]
	a['measure'] = ing_line[2].strip()
	return a


def txt_to_dict(file_name, dict):
	'''Основная функция, конвертирующая наш файл в словарь. Принимает в качестве аргументов имя файла и название
	словаря'''
	with open(file_name, 'r') as file:
		for line in file:
			if len(line) == 2:
				pass
			elif len(line) == 1:
				pass
			elif '|' not in line:
				temp = line.strip()
			elif '|' in line:
				dict.setdefault(temp, [])
				dict[temp].append(ingredient(line))
	return dict

print(txt_to_dict('recipes.txt', cook_book))

