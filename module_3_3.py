def print_params(a=1, b='STROKA', c=True):
    print(a, b, c)


print_params()
print_params(b = 123)
print_params(c = [1, 2, 3])
print()

values_list = [123, 'ABC', False]
values_dict = {'a': 321, 'b': 'CBA', 'c': False}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [2024, 'stroka']
print_params(*values_list_2, 42)
