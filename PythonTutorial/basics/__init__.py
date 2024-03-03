

def func():
    list1 = [1, 2, 3, 4]

    for i in range(0, len(list1)):
        print(list1[i])

    print(list1.pop(0))
    print(list1.count(2))

    a = 10
    print(id(a))

    b = 'some value'
    b1 = "some value"

    print(id(b))
    print(id(b1))

    # true , value same
    print(b1 == b)

    print("py " * 2)

    x = 100
    y = 100

    # same location
    print(id(x), id(y))
