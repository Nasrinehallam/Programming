import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):
    #convert theta to radians
    theta_rad= math.radians(theta)
    x= r* math.cos(theta_rad)
    y= r* math.sin(theta_rad)
    return (round(x,5),round(y,5))

r= float(input("enter the r value:"))
theta= float(input("enter the value of theta (in degrees):"))
print(polar_to_cartesian(r,theta))

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    return (0, 0)

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    return 0