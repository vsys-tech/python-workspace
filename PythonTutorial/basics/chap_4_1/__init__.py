def parrot(voltage, action="act on", on="data", type="icy blue"):
    print("getting voltage", voltage, "and action", action, "and on", on, end="\n")


def parrotCaller():
    parrot(1000)
    parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments


def cal_total(principal, **keywrods):
    total = principal
    val = []
    for key, value in keywrods.items():
        val.append(keywrods.get(key))

    for value in val:
        total += value

    print("total-> ", total)


def cal_total_caller():
    cal_total(61716.98, extra=62525.2627, other=872.27)


if __name__ == '__main__':
    pass
