def list_func(*values, **dict_values):
    print(values, dict_values)


if __name__ == '__main__':
    list_func([1, 2, 3, 4], {'a': 1, 'b': 2})
    pass
