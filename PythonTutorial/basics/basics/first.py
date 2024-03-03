"""
    1. basics
    2. flow ... loop if else for while
    3. data types
    4. any other
    5. tricks
    6. short-cuts
"""

real = 3
imaginary = 5

z = complex(real, imaginary)
# print(z)

list1 = [1, 2, 3, 4]

# list []

# print(list1)

list1 = ["some ", 1, 2, 3, 1.23, 100, 1 + 3J]

# print(list1)

tuple1 = (1, 2, 3, 4)

# print(tuple1)

# tuple can contain other objects
# ()
tuple1 = (list1, "some", 1.23, 2 + 3j)

# print(tuple1)
"""
    prints the value when assigned to other var
"""
a = tuple1[0]

# print(a)

# for i in range(0, 4, 3):
#     print(i)


dict1 = {"1": 1, "2": 2, "3": 3}

for key, value in dict1.items():
    print(key, value)

