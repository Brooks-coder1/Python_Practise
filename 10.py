# 10. Number Expansion Calculator

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

n = input("Enter the number : ")
num1 = int("%s" % n)
num2 = int("%s%s" % (n, n))
num3 = int("%s%s%s" % (n,n,n))
print(num1 + num2 +num3)