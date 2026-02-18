# 23. String Prefix Copies

# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

def copy(str, n):
    if len(str) < 2:
        return (str + " ") * n
    else:
        return str[:2] * n

str = input("Enter the text : ")   
n = int(input("Enter the number of copies : ")) 
print(copy(str, n))
