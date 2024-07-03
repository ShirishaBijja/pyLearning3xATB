# File IO

with open('example.txt','r') as file:
    print(file.read())
    file.close()  # Close has to be executed

# FileNotFoundError