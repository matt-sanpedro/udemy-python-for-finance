# tuples are the default sequence type in python

# pack three values into a tuple
my_tuple = 50, 51, 52
print(my_tuple)

# tuple unpacking
a, b, c = my_tuple
print(c)

# string manipulation with tuple unpacking
age, years_of_school = "30,17".split(",")
print(age, type(age))

# return a tuple from a function
def square_info(x):
    area = x ** 2
    perimeter = 4 * x
    return area, perimeter

print(square_info(3))
