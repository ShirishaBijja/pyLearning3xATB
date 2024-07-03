# Multiple conditions
# Switch in Java
# Match case in Python

number = int(input("Enter a number\n"))
match number:
    case 1:
        print("Hello")
    case 2:
        print("Bye")


browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "Chrome":
        print("Chrome code executed")
    case "firefox":
        print("FF code executed")
    case "Edge":
        print("Edge code executed")
    case _:
        print("No browser found")