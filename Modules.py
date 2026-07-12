#..........................Part A – Math Module..........................
# Import the math module
import math
# Find the square root of 144. 
print("√144 =" , math.sqrt(144))
# Find 7⁴ using math.pow().
print("7⁴ =", math.pow(7,4))
# Print the value of math.pi.
print("π =", math.pi)
# Calculate the area of a circle with a radius of 10.
radius=10
print("area =", math.pi*10**2)

#.......................Part B – Random Module ..........................
import random
# Generate a random number between 50 and 100.
random_number=random.randint(50,100)
print("random_number =", random_number)
# Generate a 6-digit OTP.
otp=random.randint(100000, 999999)
print("otp =", otp)
# Create a list of five fruits and randomly print one fruit using random.choice().
a=["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("random choice =", random.choice(a))

#.......................Part C – Date & Time.............................
# Print the current date and time.
from datetime import datetime
print("current date and time =", datetime.now())
# Print today's date only.
from datetime import date
print("current date =", date.today())
# Display the message "Program Started", wait for 3 seconds, then display "Program Finished".
import time
print("Program Started")
time.sleep(3)
print("Program Finished")


