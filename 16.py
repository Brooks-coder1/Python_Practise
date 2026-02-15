# 16. Difference from 17

# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference

while True:
    num = int(input("Enter a number : "))
    a = num - 17
    if num > 17 :
        print(a*2)
    elif num < 17 :
        print(abs(a))
    else:
        print("wait, something was wrong with you !")