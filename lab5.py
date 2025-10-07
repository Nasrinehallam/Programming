# Function hollow_square(n) will return a string representing a hollow square pattern of stars (*) with side length n.
# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n < 1:
        return ""
    if n == 1:
        return "*\n"
    
    square = ""
    for i in range(n):
        if i == 0 or i == n - 1:
            square += "*" * n + "\n"
        else:
            square += "*" + " " * (n - 2) + "*\n"
    return square
# Code test for hollow_square function
print(hollow_square(5))


# Function number_pattern(n) will return a string representing a number pattern of height n without using a for loop inside the print statement.
# 1
# 12
# 123
# 1234
def number_pattern(n):
    pattern = ""
    i = 1
    while i <= n:
        j = 1
        line = ""
        while j <= i:
            line += str(j)
            j += 1
        pattern += line + "\n"
        i += 1
    return pattern
# Code test for number_pattern function
print(number_pattern(4))


# Function sum_of_natural_numbers(n) will return the sum of the first n natural numbers using a while loop.
# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total
# Code test for sum_of_natural_numbers function
print(sum_of_natural_numbers(5))  # Output: 15


# Function centered_star_pyramid(n) will return a string representing a centered pyramid of stars (*) with height n.
# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    pyramid = ""
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        pyramid += spaces + stars + "\n"
    return pyramid
# Code test for centered_star_pyramid function
print(centered_star_pyramid(4))
