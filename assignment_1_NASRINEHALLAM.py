# Function 1:
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    return max(num1, num2, num3)
# Code test for Function 1
print(built_in_functions_max(3, 5, 2))  # Output: 5
print(built_in_functions_max(12, 111, 1234)) # Output: 1234

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    return min(num1, num2, num3)
# Code test for Function 2
print(built_in_functions_min(3, 5, 2))  # Output: 2
print(built_in_functions_min(12, 111, 1234)) # Output: 12

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
# Code test for Function 3
print(check_number(10))  # Output: Positive
print(check_number(-5))  # Output: Negative
print(check_number(0))   # Output: Zero

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    shape = ""
    for i in range(1, rows + 1):
        shape += "*" * i + "\n"
    return shape
# Code test for Function 4
print(star_shape(5))

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    result = []
    num = 1
    while num <= limit:
        if num % 3 == 0:
            result.append("Multiple of 3")
        else:
            result.append(num)
        num += 1
    return result
# Code test for Function 5
print(count_multiples_of_3(10))  # Output: [1, 2, 'Multiple of 3', 4, 5, 'Multiple of 3', 7, 8, 'Multiple of 3', 10]

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total
# Code test for Function 6
print(sum_of_even_numbers(1, 10))  # Output: 30
print(sum_of_even_numbers(0, 20))  # Output: 110

