# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number):
    if day_number < 1 or day_number > 7:
        return "Not a proper day number" 
    elif 1 <= day_number <= 5:
        return "It is a Weekday!"  
    else:
        return "It is a Weekend!"
# Input
day_number = int(input("Enter a day number (1-7): "))
# Output
print(check_weekday_or_weekend(day_number))

# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number):
    if day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    elif day_number == 7:
        return "Sunday"
    else:
        print("Not a proper day number")

# Input
day_number = int(input("Enter a day number (1-7): "))
# Output
print(get_day_name(day_number))
