# 7. File Extension Extractor

# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java


user = input("Enter Your File name : ")
output = user.split(".")
print(f"The extension of {user} is {output[-1]}")