# 1st parameter - File.fileformat
# 2nd parameter - File Operation

'''
File operations
r - read
w - write
a - append
x - create

File Functions
close() - close the file
read() - read the file
readline() - reads the line per character - parameter num of character you want to show
readlines() - reads the file per line
write() - writes on the file
'''
# Open the file in read mode
file = open('day-06\example.txt', "r") 
# i used the files relative path so when someone runs it into their local machine, it can always run. avoid hardcoded path
# Read and print the content
content = file.read()
print(content)
file.close()

