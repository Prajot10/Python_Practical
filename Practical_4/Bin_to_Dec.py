# P4 (Q.2) - Python program to convert number Binary to Decimal.


def Binary_to_Decimal(num):
    return int(num , 2)

num = str(input("Enter Binary number : "))
print("Decimal number :", Binary_to_Decimal(num))