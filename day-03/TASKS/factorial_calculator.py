# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.
print("FACTORIAL CALCULATOR FOR ALF")
input = int(input("Please, enter a non-negative integer: "))

  
  

# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.
num = input # pass the value of input to num 
result = 1 # initialize starting value

while num > 0:
  result *= num
  num -= 1 # so the loop continues
# Write the code ↓ to display the factorial result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The factorial of " + str(input) + " is " + str(result))





''' 
Pseudocode
1. User inputs a non-negative integer
2. Loop 
  - As long as (while) input is greater than 0, the factorial would be calculated. 
    - Ex. input = 5. 5x4x3x2x1 = 120
    - input * input-1 ---> but the problem  in this is the input should be CONTINUOUSLY multiplied by its lesser number thus the *=
    - result = num *= num -1 ---> this code won't work, we need to do it bit by bit
    - final: result *= num
    - counter: num -= 1 (this should progress the loop)
3. Print result
'''