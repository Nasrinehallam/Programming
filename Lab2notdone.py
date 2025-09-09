# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # TODO: Implement this function
    g = 9.8
    H0 = float(h0) - 1/2 * g * float(t)**2
    print('Height of the ball at' + str(t) + 'seconds =' + str(H0) + 'METERS')
h0 = float(input('what is the initial height?'))
t= float(input('what is the time'))
calculate_height(h0, t)
# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code