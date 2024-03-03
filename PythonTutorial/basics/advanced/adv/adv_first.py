
def make_upper(text):
    return text.upper()


def make_lower(text):
    return text.lower()


def greet(text, func_ref):
    print(func_ref(text))
    # greet(text="here is some text", func_ref=make_upper)
    # greet(text="HOW COME CHANGE THE CASE", func_ref=make_lower)


def add(x):
    def add_to(y):
        print(x + y)

    return add_to;
#    add(10)(20)

