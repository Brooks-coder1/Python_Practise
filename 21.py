# 21. Even or Odd Checker

# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def num_checker(n):
    if n%2==0:
        print(f"This {n} is Even")

    else:
        print(f"This {n} is Odd number")
    
n = int(input("Enter a number : "))
print(num_checker(n))

