# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.
print("PERFECT NUMBER DENOMINATOR FOR ALF")
while True: 
  str_user_input = input("Please, enter a positive integer: ")
  
  try: 
    user_input = float(str_user_input)
    if user_input >= 0 and user_input.is_integer(): # input should be positive integer
      user_input = int(user_input)
      result = 0

# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.
      for divisor in range(1, user_input): # parameter is start 1, end with the value of input
        if user_input % divisor == 0:
          result += divisor

# Write the code ↓ to display the Perfect Number check result.
# NOTE : You can use if-else statement or ternary operator to display the result.
      if result == user_input:
          print(str(user_input) + " is a Perfect number.")
      else:
          print(str(user_input) + " is not a Perfect number.")
      break # stops the program from asking user_input  again and again.
    else:
      print("Invalid Input. Please try again")
    
  except ValueError:
    print("Invalid Input. Please try again")


