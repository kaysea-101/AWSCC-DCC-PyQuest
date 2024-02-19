import math
print("CYLINDER VOLUME CALCULATOR FOR ALF")
# Write the code ↓ to read the radius and height of a cylinder from the user.
# Be cautious when reading input of various data types.
while True:
  try:
    str_radius = input("Please, enter the radius of the cylinder: ")
    str_height = input("Please, enter the height of the cylinder: ")

    radius = float(str_radius)
    height = float(str_height)


# Write the code ↓ to calculate the volume of the cylinder using the formula V = πr^2h.
# Formula to calculate the volume (V) of a cylinder:
# V = π * r^2 * h
    if height > 0 and radius > 0:
      power_radius = math.pow(radius, 2)
      result = math.pi * power_radius * height
      rounded_result = round(result, 2)
      break

    elif height <= 0 and radius > 0:
      print("Invalid input. Radius should be greater than 0.")

    elif height > 0 and radius <= 0:
      print("Invalid input. Radius should be greater than 0.")
      
  except ValueError:
    print("Invalid Input. Try to input a float value")
    
# Write the code ↓ to display the calculated volume with 2 decimal places.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The volume of the cylinder is: " + str(rounded_result))

