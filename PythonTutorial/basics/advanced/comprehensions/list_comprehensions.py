def list_some_ex():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    elist = [e_num for e_num in list1 if e_num % 2 == 0]
    olist = [o_num for o_num in list1 if o_num % 2 != 0]

    t = [(x, y) for x, y in zip(elist, olist)]

    print(t)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    transposed = [[row[col] for row in matrix] for col in range(3)]
    print(transposed)

    list2 = list(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']))

    print(list2)

    text = "python"
    print(list(text))


def zipping_2_lists():
    list1 = ["Hello ", "Hi ", "How "]
    list2 = ["World", "There", "are you?"]
    [print(i + j) for i, j in zip(list1, list2)]


# range generator...
def list_iter(num):
    yield [num for num in range(num)]
    # x= list_iter(10)
    # print(next(x))


def get_str():
    return lambda s: ''.join([ch for ch in s if not ch.isdigit()])
    # print(get_str()("kjs4455akdjka"))


def sum_all():
    list1 = [1, 2, 3, 4]
    print(sum(list1))


def find_sum():
    return lambda num: sum([int(x) for x in str(num)])
    # print(find_sum()(7678))


def sortedList():
    list1 = ['3', '123', '-1', '0']
    print(sorted(list1, key=lambda num: int(num)))


def filter_List():
    list1 = ['3', '123', '-1', '0']
    print(list(filter(lambda num: int(num) > 0, list1)))


def map_List_ex1():
    list1 = ['hello', 'world', 'made', 'upper']
    print(list(map(lambda s: str.upper(s), list1)))


def map_List_ex2():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(list(filter(lambda num: num % 2 == 0, list1)))


def merge_2_lists():
    list1 = [9, 1, 2, 2, 5, 6, -3]
    list2 = [2, 3, 5, 7, 8, -1]
    print(sorted(list(set(list1) | set(list2))))


if __name__ == '__main__':
    merge_2_lists()
    pass
