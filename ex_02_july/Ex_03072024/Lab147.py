# try, except and finally

try:
    num1 = int(input("Enter a number 1 \n"))
    num2 = int(input("Enter a number 2 \n"))
    result = num1/num2
    print(result)
except Exception as e:
    print(e)