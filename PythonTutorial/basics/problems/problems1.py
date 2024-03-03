def buildArray(nums: list[int]) -> list[int]:
    new_nums = []
    for i in range(len(nums)):
        if len(nums) > nums[i]:
            new_nums.append(nums[nums[i]])

    return new_nums


def main1():
    list1 = [0, 2, 1, 5, 3, 4]
    print(buildArray(list1))
    pass


def getConcatenation(nums: list[int]) -> list[int]:
    print(nums * 2)
    pass


def main2():
    list2 = [1, 2, 1]
    print(getConcatenation(list2))


def numIdenticalPairs(nums: list[int]) -> int:
    count = 0
    n = range(len(nums))

    for i in n:
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count = count + 1

    return count


def main3():
    list3 = [1, 2, 3, 1, 1, 3]
    print(numIdenticalPairs(list3))


def shuffle(nums: list[int], n: int) -> list[int]:
    new_nums = []
    for i in range(n):
        new_nums.append(nums[i])
        new_nums.append(nums[n])
        n += 1

    return new_nums


def main4():
    list4 = [1, 2, 3, 4, 4, 3, 2, 1]
    n = len(list4) // 2
    print(shuffle(list4, n))


def findWordsContaining(words: list[str], x: str) -> list[int]:
    list1 = []
    for i in range(len(words)):
        if x in words[i]:
            list1.append(i)
    return list1


def main5():
    # words = ["leet", "code"], x = "e"
    # words = ["abc", "bcd", "aaaa", "cbc"], x = "a"
    # words = ["abc","bcd","aaaa","cbc"], x = "z"
    print(findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="z"))


# main1()
# main2()
# main3()
# main4()
main5()
