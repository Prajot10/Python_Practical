# P-6 Q-2) Program to remove the ith occurrence of given word in a list where words repeat

list1= ["apple","apple","mango","mango","apple","banana","cherry"]
word = "apple"
n = 3
count = 0
index = 0
for i in list1:
    index += 1
    if i == word:
        count += 1
        if count == n:
            list1.pop(index-1)
print(list1)
