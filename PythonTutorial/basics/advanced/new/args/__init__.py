"""
    *args
    **kwargs
"""


def print_arr(*args):
    for arg in args:
        print(arg)


def print_arr_pos(arg, *args):
    print("pos -> ", arg)
    print(args)


def print_dict_kw(**kwargs):
    print(kwargs)


print_arr('1', '2', '3')
print_arr_pos('a', 'sdkajdkjkj', 'skdjkadjkj')

# positional arguments as keywords prints as json/ javascript object/ dict
print_dict_kw(a='jaja', b='2', c='dd')
