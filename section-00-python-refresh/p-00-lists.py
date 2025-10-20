participants = ["Alice", "Bob", "Charlie", "Diana"]
print(participants.index("Bob"))

newcomers = ["Matt", "Naomi"]
bigger_list = participants + newcomers
print(bigger_list)

bigger_list.sort(reverse=True)
print(bigger_list)

bigger_list.sort()
print(bigger_list)

numbered_list = list(range(1,11))
print(numbered_list)

numbered_list.sort(reverse=True)
print(numbered_list)

# print the first four numbers from the list
print(numbered_list[:4])

# Using slicing, extract all the elements from the list from the 3rd position onwards
print(numbered_list[2:])

# Using slicing, extract the last 4 elements from the list
print(numbered_list[-4:])

# position of 10 in the numbered list
print(numbered_list.index(10))
