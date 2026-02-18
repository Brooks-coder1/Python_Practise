# 24. Vowel Tester

# Write a Python program to test whether a passed letter is a vowel or not.

def vowel(a):
    if a in ["a", "e", "i", "o" , "u"]:
        return print("yes")
    elif len(a) > 1:
        print(f"just enter one letter not {len(a)} ")
    else:
        print("No")
while True : 
    a = input("Enter a letter : ")
    vowel(a)