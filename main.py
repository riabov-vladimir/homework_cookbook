with open('recipes.txt', 'r') as file:
	print(file.read())

cook_book = {'dish': [{'ingredient_name': [], 'quantity': [], 'measure': []}]}
a = {'ingredient_name': None, 'quantity': None, 'measure': None}
# b = '666'
# a['quantity'].append(b)

print(a)

c = 'Винный уксус | 1 | ст.л'

d = c.split(' | ')
print(d)
a['ingredient_name'] = d[0]
a['quantity'] = d[1]
a['measure'] = d[2]

print(a)