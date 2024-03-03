def runningSum(nums: list[int]) -> list[int]:
    running_sum_arr = []

    for i in range(len(nums)):
        running_sum_arr.append(sum(nums[:i + 1]))
    return running_sum_arr


def main1():
    # nums = [1, 2, 3, 4]
    # nums = [1, 1, 1, 1, 1]
    nums = [3]
    print(runningSum(nums))
    pass


def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    count_list = []
    for i in range(len(nums)):
        count = 0
        for j in range(0, len(nums)):
            if i != j and nums[i] > nums[j]:
                count += 1

        count_list.append(count)

    return count_list


def main2():
    # nums = [8, 1, 2, 2, 3]
    # nums = [6, 5, 4, 8]
    nums = [7, 7, 7, 7]
    print(smallerNumbersThanCurrent(nums))
    pass




# main1()
main2()
