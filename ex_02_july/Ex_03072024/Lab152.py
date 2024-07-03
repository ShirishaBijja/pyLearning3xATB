# File IO
import os.path
try:
    file = open('example.txt','r')
    print(file.read())
except FileExistsError as fnfe:
    print("I am not able to find the file. please check")
finally:
    print("Executed")
    try:
        file.close()  # Close has to be executed
    except NameError as ne:
        print(ne)