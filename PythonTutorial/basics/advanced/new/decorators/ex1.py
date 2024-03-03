# decorator
"""
    

"""


def outer_func(func):
    def inner_func():
        print("before calling func")

        func()

        print("after calling func")

    return inner_func


@outer_func
def calling_func():
    print("execution of main function")


if __name__ == '__main__':
    # calling_func = outer_func(calling_func);
    calling_func()
