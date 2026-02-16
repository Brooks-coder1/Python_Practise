# 22. Count 4 in List

# Write a Python program to count the number 4 in a given list.

def count_num_4(nums):
    count = 0
    for num in nums:
        if num == 4 :
            count = count + 1

    return count

a = input("Enter a list : ")
nums = a.split(",")

nums = [int(i) for i in nums ]

print(count_num_4(list(nums)))



