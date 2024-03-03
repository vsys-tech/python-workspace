def _find_max(values):
    _max = values[0]
    values = values[1:]

    for i in range(len(values)):
        _val = values[i]
        _max = ((_max, _val)[_max < _val])
    return _max


def _find_max_dc(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        m = _find_max_dc(list1[1:])
        m = m if m > list1[0] else list1[0]

    return m


def main1():
    arr = list(map(int, input("enter values to find the max :  ").strip().split()))
    print(_find_max(arr))


def main2():
    arr = list(map(int, input("enter values to find the max :  ").strip().split()))
    print(_find_max_dc(arr))


# main1()
main2()
