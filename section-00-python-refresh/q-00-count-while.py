"""
Docstring for q-00-count-while

Conditional Statements, Functions, and Loops - Exercise #1

You are provided with the nums list. Define a function called count() containing 
a while loop to count the number of values in the nums list that are lower than 20.
"""
nums = [1,35,12,24,31,51,70,100]

# print(len(nums))

def count(nums):
    total = 0
    i = 0

    while i < len(nums):
        if nums[i] < 20:
            total += 1
        i += 1

    return total

print(count(nums))
