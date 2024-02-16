# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.
print("SIMPLE CALCULATOR FOR ALF\n")
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x , /): ")

# Write the code ↓ to perform the calculations based on the selected operation.
if operator == "+":
  result = first_num + second_num
  
elif operator == "-":
  result = first_num - second_num

elif operator == "x":
  result = first_num * second_num

elif operator == "/":
  result = first_num / second_num


# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The result of " + str(first_num) + " " + operator + " " + str(second_num) + " is " + str(result))






