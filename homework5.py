immutable_var = 5, 'house', 6.88, 'x = 3'
print(immutable_var)
immutable_var [4] = 1000
 # Кортеж нельзя изменить, он являетсся ссылкой на список, а не самим списком, предназначен только для чтения.

mutable_list = [1, 35, 'car', 5.4]
print(mutable_list)
mutable_list.append('big_smoke')
print(mutable_list)