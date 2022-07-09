# Write telephone directory of 10 students using dictionary and perform operation
# A) finding value-key:value
# B) replacing value-key: new value
# C) replacing key value - delete key and insert new key

tel_dir = {"Prajot": 9876543210, "Prasad": 9876543211, "Mama": 9876543212, "Aai": 9876543213, "Mammi": 9876543214,
           "Mummy": 9876543215, "Prerana": 9876543216, "Mayur": 9876543217, "Didi": 9876543218, "Chaitu": 9876543219}
print("Telephone directory is :")
print(tel_dir)
# A) finding value-key:value
key = str(input("Enter key to find value : "))
print("Telephone number of given key " + key + " is :")
for i in tel_dir.keys():
    if i == key:
        print(tel_dir[i])


# B) replacing value-key : new value
key = str(input("Enter key to find value : "))
value = str(input("Enter new value :"))
for i in tel_dir.keys():
    if i == key:
        tel_dir[i] = value
print("Telephone directory after replacement :")
print(tel_dir)

# C)replacing key value -delete key and insert new key

num = int(input("Enter telephone number : "))
name = str(input("Enter new key name : "))
old_key = 0
for key, value in tel_dir.items():
    if num == value:
        old_key = key
tel_dir[name] = tel_dir.pop(old_key)

print("Dictionary after replacing key:value :")
print(tel_dir)