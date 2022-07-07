# P4 (Q.2) - Python program to convert number Decimal to Binary.

def Decimal_to_Binary(num):
    if num > 1:
        Dec_to_Bin(num//2)
    print(num%2 , end="")
num = int(input("Enter Decimal number : "))
Decimal_to_Binary(num)