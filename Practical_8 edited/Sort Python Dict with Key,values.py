# P8 Q.1(b) Sort dictionary by Values.

dict1 = {1: 9, 2: 8, 3: 7}
sorted_values = sorted(dict1.values()) # Sort the values 7,8,9
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)