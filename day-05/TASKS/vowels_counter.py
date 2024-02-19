# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.
print("VOWEL COUNTER FOR ALF")
word = input("Please, enter a word/s to check: ")






# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.
occurences_a = word.count("a")
occurences_e = word.count("e")
occurences_i = word.count("i")
occurences_o = word.count("o")
occurences_u = word.count("u")
result = occurences_a + occurences_e + occurences_i + occurences_o + occurences_u 

# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The number of vowels in " + "'"+ word + "' is: " + str(result))        





