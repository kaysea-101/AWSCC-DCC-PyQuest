# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.
print("PALINDROME CHECKER FOR ALF")
word = input("Please, enter a word/s to check: ")

# Write the code ↓ to check if the entered word is a palindrome.
# Utilize string functions to compare the original word with its reverse.
reversed_word = word[::-1]
print("reversed word: " + reversed_word)

# Write the code ↓ to display whether the entered word is a palindrome or not.
# Select and employ a string concatenation method based on your personal preference and comfort level.
if word == reversed_word: 
  print("'" + word + "'" + " is a palindrome")
  
else:
  print("'" + word + "'" + " is NOT a palindrome")



