# P4 (Q.1) - Python program to Print Perfect Number.

# Sum of factors equal to given number.
# num = 28
# 28 is perfect number.

Num = int(input("Enter any number - "))
Factor = []
for i in range(1,Num):
    if Num%i==0:
        Factor.append(i)
summ=sum(factor)
if summ==Num:
    print(Num,"is a Perfect Number.")