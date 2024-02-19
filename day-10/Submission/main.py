import json

# prompt the user to input data
input_name = input("Enter your name: ")
input_age = input("Enter your age: ")
input_favefood = input("Enter your favorite food: ")

# encode to dictionary
data = {
    "name": input_name,
    "age": input_age,
    "favorite food": input_favefood
}

# write the data on json
content = json.dumps(data, indent=2)

# display the data
print(content)

# save the data to the file output.json
output_file_path = 'day-10/output.json' 

with open(output_file_path, 'a') as file:
    file.write(content + ' \n') # so in json the data will be on a new line
    print("The data has been saved successfully.")

