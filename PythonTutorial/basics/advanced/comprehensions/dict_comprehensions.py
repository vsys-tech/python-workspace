list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

dict1 = {(k, v) for k, v in zip(list1, list2)}
print(sorted(dict1))
