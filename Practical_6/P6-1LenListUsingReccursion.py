# Q.1 ) Python program to find list of list using recursion

list1 = [1, 2, 3, 4, 5, 6]

if not list1:
    print(0)
else:
    print(1 + len(list1[1::2]) + len(list1[2::2]))

