import os

file = open("data.txt", mode='r+')

# file.write("some  again")
data = file.readlines()
for eac_line in data:
    print(eac_line.split())
file.close()
