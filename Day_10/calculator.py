print(
    """ 
 _____________________
|  _________________  |
| | PYTHONISTA   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator(a, b, operator):
    return operations[operator](a, b)


a = int(input("Enter a: "))

while True:
    b = int(input("Enter b: "))
    operator = input("Enter the operator (+, -, *, /): ")
    result = calculator(a, b, operator)
    print(f"{a} {operator} {b} = {result}\n")
    again = (
        input(f"Do you want to continue calculating with {result}? (y/n): ").lower()
        == "y"
    )
    if not again:
        break

    a = result
