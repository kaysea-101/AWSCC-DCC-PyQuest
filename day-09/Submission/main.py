
file_path = 'day-09\story.txt' # story.txt file

with open(file_path, 'r') as file: # open and read file
  reader = file.readlines() # line by line
  total_lines = len(reader) # count the lines
  
  # display the result
  print("The total number of lines in this file is " + str(total_lines) + ".")
    