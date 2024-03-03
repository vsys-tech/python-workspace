import random
import textwrap


# list1 = [1, 2, 3, 456, 5, 6, 7, 8, 9, 10]
#
# # choice of values
# print(random.choice(list1))
#
# # shuffle list
# random.shuffle(list1)
# print(list1)
#
# random.seed(100)
# print(round(random.random(), 2))
# print(round(random.random(), 2))


# list1 = [1, 2, 3, 4, 5, 78, 45, 23]
# set1 = set(list1)
# set1.remove(max(set1))
# print(max(set1))

def find_sec_last1():
    scores = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
    val_list = dict(scores).values()
    sorted_val_list = sorted(set(val_list))
    arr = [k for k, v in dict(scores).items() if v == sorted_val_list[1]]
    arr = sorted(arr)
    for i in range(len(arr)):
        print(arr[i])


def find_avg():
    scores = {'Harsh': [20, 30, 24], 'Beria': [30, 40, 50]}
    name = "Beria"
    marks = list(dict(scores).get("Beria"))
    print("{:0.2f}".format(sum(marks) / len(marks)))
    # find_avg()


def wrap_string():
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    n = 4
    wrapper = textwrap.TextWrapper(width=n)
    return wrapper.fill(text=string)


if __name__ == '__main__':
    print(wrap_string())
