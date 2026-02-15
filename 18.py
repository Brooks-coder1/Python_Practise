# 18. Triple Sum Calculator

# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def triple_sum(a,b,c):
    sum  = a +b +c

    if a == b ==c :
        sum = sum*3
    
    return sum

a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
c = int(input("Enter third value : "))

print(triple_sum(a,b,c))