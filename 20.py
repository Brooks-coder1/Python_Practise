# 20. String Copy Generator

# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.


def copy(text, n):
    return (text+ " ")*n

text = input("Enter the text to copies : ")
n = int(input("Enter the number of copies : "))

print(copy(text, n))