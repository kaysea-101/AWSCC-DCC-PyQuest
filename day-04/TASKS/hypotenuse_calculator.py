import math
# Write the code ↓ to calculate the hypotenuse using the Pythagorean theorem.
# The Pythagorean theorem: c^2 = a^2 + b^2, where c is the hypotenuse.
# Write the code ↓ to display the calculated hypotenuse.
# Select and employ a string concatenation method based on your personal preference and comfort level.
def calculate_hypotenuse(input_a, input_b): # parameter name can be different
  power_a = math.pow(input_a, 2)
  power_b = math.pow(input_b, 2)
  result = math.sqrt(power_a + power_b)
  rounded_result = round(result, 2)
  print("The hypotenuse of the right-angled triangle is: "+ str(rounded_result)) # always convert to string whenever there is a string "value" with any numerical.
  return rounded_result


# Write the code ↓ to read the lengths of the two shorter sides of a right-angled triangle from the user.
# Be cautious when reading input of various data types.

while True: # the program can ask again when the program catches an error (alphabets) on the input.
  try:
    str_input_a = input("Please, enter the length of side A: ")
    str_input_b = input("Please, enter the length of side B: ")

    input_a = float(str_input_a)
    input_b = float(str_input_b)
  
    if input_a > 0 and input_b > 0:
      rounded_result = calculate_hypotenuse(input_a, input_b)
      break # break stops the program from asking for input again.

    elif input_a <= 0 and input_b > 0:
      print("Invalid Input. Side A must be greater than 0.")
      

    elif input_a > 0 and input_b <= 0:
      print("Invalid Input. Side B must be greater than 0.")
      
    
  except ValueError:
    print("Invalid Input. Try again with float value.")
    # the display here only works after the user has input on both a and b. (after b it shows the string Invalid Input given that the user inputs an Invalid input on input_a or input_b)

# kahit pala hindi i-function HAHAHAHAHA bwct


