def func():
    """this is just doc
    """
    pass


def f(ham: str, eggs: str = "eggs"):
    print("annotations", f.__annotations__)
    print("argu", ham, eggs)
    print(ham + " and " + eggs)
    pass


def add_array(a, arr=[]):
    arr.append(a);
    print(arr)


i = 5


def value_default(a=i):
    print(a)


if __name__ == '__main__':
# print(func.__doc__)
# f("spam")
# add_array(1)
# add_array(2)
# add_array(3)
# value_default()
    pass
