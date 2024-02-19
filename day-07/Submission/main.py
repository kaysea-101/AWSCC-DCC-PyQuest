import os


# select which path the file will be created
folder_path = "day-07\Submission" 
file_name = "user_info.txt"
file_path = os.path.join(folder_path, file_name)

# ask user for their name
name = input("Enter your name: ")
# open and write on the file 
with open(file_path, "a") as file: # 2 parameters
  file.write(name + '\n')
  print(name + " written successfully on a file named " + file_name)

file.close()