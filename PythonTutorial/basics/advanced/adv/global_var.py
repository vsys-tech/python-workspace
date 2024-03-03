s = " hi there"


def change_to_local():
    global s
    s += ""
    print(s)
    s = "changing to hello there "
    print(s)
    # change_to_local()


list1 = [1, 2, 3, 4]


def change_global_list():
    for i in range(4):
        list1[i] = list1[i] + i

    return list1
    # print(change_global_list())


if __name__ == '__main__':
    pass
