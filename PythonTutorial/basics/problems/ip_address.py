_ip_str = "1.1.1.1"


def modify_ip_str(_ip_str):
    print(str.replace(_ip_str, ".", "[.]", -1))


def main1():
    _ip_str = input("Enter IP Address: ")
    modify_ip_str(_ip_str)


def math_ops(operations) -> int:
    x = 0
    for op in operations:
        match op:
            case '--X' | 'X--':
                x = x - 1
            case 'X++' | '++X':
                x = x + 1
            case default:
                print("Invalid")

    return x


def main2():
    operations = input("Enter the operations (sep by ',' ): ").split(",")
    print(operations)
    print(math_ops(operations))


def numJewelsInStones(jewels: str, stones: str) -> int:
    import re
    count = 0
    for j in range(len(jewels)):
        count += len(re.findall(jewels[j], stones))

    return count


def main3():
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels=jewels, stones=stones))


# main1()
# main2()
main3()
