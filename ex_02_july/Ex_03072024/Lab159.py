# File Handling
# How to Read a Text, and Write into it using Python code.

# Functions

# Read and Write content
# Read a File
# Reading Entire Content: content = file_object_read()

file = open("TestData.txt","r")
content = file.read()
print(content)
file.close()
