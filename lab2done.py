# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # TODO: Implement this function
    g = 9.8
    #This is the calculation
    H0 = float(h0) - 1/2 * g * float(t)**2

    return H0

h0 = float(input('what is the initial height?'))
t= float(input('what is the time'))
H0=calculate_height(h0, t)
calculate_height(h0, t)
print('Height of the ball at' + str(t) + 'seconds =' + str(H0) + 'METERS')


# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    speed=20
    Distance = speed * float(t)
    Final_distance= int(Distance)
    return Final_distance

    # TODO: Implement this function
t = input("Enter time for car (in seconds):")
Final_distance=calculate_car_distance(t)
calculate_car_distance(t)
print("the car will travel" + str(Final_distance)+ " meters in " + str(t) + "seconds")

