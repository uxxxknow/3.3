# 1. Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()      # Функцию с разным количеством аргументов вывести нельзя, потому что количество аргументов должно равняться количеству параметров. Без аргументов можно, если они указаны по умолчанию(как сделано у нас).
print_params(b = 25)
print_params(c = [1,2,3])

# 2. Распаковка параметров:
values_list = [False, 5, 'string']
values_dict = {'a': 'hello', 'b': True, 'c': 10}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры:
values_list_2 = [True, 3]
print_params(*values_list_2, 42)          # Работает, т.к. теперь количество аргументов совпадает с количеством параметров, созданной функции.






# values_list_2 = [54.32, 'Строка' ]
# print_params(*values_list_2, 42)