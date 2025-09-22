import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):
    # Convert polar (r, theta_in_degrees) -> Cartesian (x, y). Returns (x, y) rounded to 5 decimal places.
    theta_rad= math.radians(theta)
    x= r* math.cos(theta_rad)
    y= r* math.sin(theta_rad)
    return (round(x,5),round(y,5))
#the lines 10-13 are for testing the function
r= float(input("enter the r value:"))
theta= float(input("enter the value of theta (in degrees):"))
print(polar_to_cartesian(r,theta))

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r = math.hypot(x, y)           # sqrt(x**2 + y**2)
    theta_rad = math.atan2(y, x)   # handles quadrant correctly
    theta_deg = math.degrees(theta_rad)
    return (round(r, 5), round(theta_deg, 5))

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    omega = 2 * math.pi * f
    phi_rad = math.radians(phi)
    x = A * math.cos(omega * t + phi_rad)
    return round(x, 5)