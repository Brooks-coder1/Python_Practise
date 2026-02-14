# 4. Circle Area Calculator

# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504


print("---------  Circle Area Calculator  -----------\n")
while True:
    user = float(input("Enter radius of circle : "))
    circle = 22/7*(user**2)
    print(f"The Area of circle is {circle}")
    print("\n----------------------------------------------------")
