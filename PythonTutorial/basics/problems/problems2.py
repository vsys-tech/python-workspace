# l1 = [3,9,1,1,5,8]
# l2 = [1,0,0,4,3,8]

def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    list1 = []
    print(map(lambda y: y[1], list1))
    return max(list1)


def main1():
    list1 = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    val = max(map(lambda point: point[1], list1))
    print(val)
    # print(maxWidthOfVerticalArea(list1))
    pass


def maximumWealth(accounts: list[list[int]]) -> int:
    max_sum = 0

    for account in accounts:
        wealth = sum(account)
        max_sum = max(max_sum, wealth)

    return max_sum


def main2():
    accounts = [[3, 1], [9, 0], [1, 0], [1]]
    print(maximumWealth(accounts))
    pass


def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
    count = 0;
    for hrs in hours:
        if hrs >= target:
            count = count + 1
    return count


def main3():
    # hours = [0,1,2,3,4], target = 2
    # hours = [5, 1, 4, 2, 2], target = 6
    print(numberOfEmployeesWhoMetTarget(hours=[5, 1, 4, 2, 2], target=6))
    pass


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    _max = max(candies)
    list1 = []
    for i in range(len(candies)):
        list1.append(candies[i] + extraCandies >= _max)

    return list1


def main4():
    # candies = [2,3,5,1,3], extraCandies = 3
    # candies = [4, 2, 1, 1, 2], extraCandies = 1
    # candies = [12,1,12], extraCandies = 10
    print(kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
    pass


def countPairs(nums: list[int], target: int) -> int:
    return len([[i, j] for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] < target])


def main5():
    # nums = [-1,1,2,3,1], target = 2
    # nums = [-6,2,5,-2,-7,-1,3], target = -2
    print(countPairs(nums=[-6, 2, 5, -2, -7, -1, 3], target=-2))


# main1()
# main2()
# main3()
# main4()
main5()
