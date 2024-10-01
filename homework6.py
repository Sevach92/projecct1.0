# Словари
my_dict = {'Всеволод': 1992, 'Андрей': 1970, 'Алла': 1971}
print(my_dict)
print(my_dict.get('Андрей'))
print(my_dict.get('Марина', 'Такого ключа не существует'))
my_dict.update({'Мария': 1994,'Даниил': 2000})
print(my_dict)
deleted = my_dict.pop('Мария')
print(my_dict)
print(deleted)
print(my_dict)

# Множества
my_set = {5, 7, 100, True, 7, 100, 5, 56.78, (4, 5,6 ,9 ,0 ,3), 56.78, (4, 5,6 ,9 ,0 ,3)}
print(my_set)
print(my_set.add('Марина'))
print(my_set.add(3465))
print(my_set)
print(my_set.discard(100))
print(my_set)

