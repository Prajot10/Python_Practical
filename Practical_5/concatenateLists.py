# 4) Python program to write a python program concatenate two lists.

list1 = ["S", "T"]
list2 = ["1", "2"]

res = [x + y for x in list1 for y in list2]
print(*res)