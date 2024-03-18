import math
import random

def add(a, b):
    a = float(a)
    b = float(b)
    print(f"Sum: {a + b}")

def multiply(a, b):
    print(f"Product: {float(a) * float(b)}")

def divide(a, b):
    a = float(a)
    b = float(b)
    if b == 0:
        print("Can't divide by zero!")
    else:
        print(f"Division result: {a / b}")

def subtract(a, b):
    a = float(a)
    b = float(b)
    print(f"Difference: {a - b}")

def square_root(a):
    a = float(a)
    if a < 0:
        b = a * -1
        print(f"Square root of {a}: {math.sqrt(b)}i")
    elif a > 0:
        print(f"Square root of {a}: {math.sqrt(a)}")
    else:
        print("Square root of 0 is 0.")

def power(a, b):
    a = float(a)
    b = float(b)
    print(f"{a} raised to the power of {b} is: {a**b}")

def cos(a):
    a = float(a)
    print(f"Cosine of {a}: {math.cos(a)}")

def sin(a):
    a = float(a)
    print(f"Sine of {a}: {math.sin(a)}")

def tan(a):
    a = float(a)
    print(f"Tangent of {a}: {math.tan(a)}")

def cot(a):
    a = float(a)
    print(f"Cotangent of {a}: {1/math.tan(a)}")

def log(a):
    a = float(a)
    if a <= 0:
        print("Logarithm is undefined for non-positive numbers.")
    else:
        print(f"Logarithm of {a}: {math.log(a)}")

def random_number(a):
    a = float(a)
    b = random.randint(1, 50)
    result = (a * b / 2 + 5) / random.randint(1, 5)
    print(f"Random number calculation result: {result}")

def factorial(a):
    a = int(a)
    if a < 0:
        print("Factorial is undefined for negative numbers.")
    else:
        print(f"Factorial of {a}: {math.factorial(a)}")

def inverse(a):
    a = float(a)
    if a == 0:
        print("Inverse of 0 is undefined.")
    else:
        print(f"Inverse of {a}: {1/a}")

def absolute_value(a):
    a = float(a)
    print(f"Absolute value of {a}: {abs(a)}")

def square(a):
    a = float(a)
    print(f"Square of {a}: {a**2}")

def main():
    while True:
        print("Welcome! Choose an operation:")
        print("1. Add")
        print("2. Multiply")
        print("3. Divide")
        print("4. Subtract")
        print("5. Square Root")
        print("6. Power")
        print("7. Cosine")
        print("8. Sine")
        print("9. Tangent")
        print("10. Cotangent")
        print("11. Log")
        print("12. Random Number Generator")
        print("13. Factorial")
        print("14. Absolute Value")
        print("15. Inverse")
        print("16. Square")
        print("17. Exit")
        
        option = input("Your choice: ")
        
        if option == "1":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            add(a, b)
        elif option == "2":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            multiply(a, b)
        elif option == "3":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            divide(a, b)
        elif option == "4":
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            subtract(a, b)
        elif option == "5":
            a = input("Enter the number: ")
            square_root(a)
        elif option == "6":
            a = input("Enter the base number: ")
            b = input("Enter the exponent: ")
            power(a, b)
        elif option == "7":
            a = input("Enter the number: ")
            cos(a)
        elif option == "8":
            a = input("Enter the number: ")
            sin(a)
        elif option == "9":
            a = input("Enter the number: ")
            tan(a)
        elif option == "10":
            a = input("Enter the number: ")
            cot(a)
        elif option == "11":
            a = input("Enter the number: ")
            log(a)
        elif option == "12":
            a = input("Enter the number: ")
            random_number(a)
        elif option == "13":
            a = input("Enter the number: ")
            factorial(a)
        elif option == "14":
            a = input("Enter the number: ")
            absolute_value(a)
        elif option == "15":
            a = input("Enter the number: ")
            inverse(a)
        elif option == "16":
            a = input("Enter the number: ")
            square(a)
        elif option == "17":
            print("Goodbye!")
            break
        else:
            print("Oops! That's not a valid option. Please try again.")

if __name__ == "__main__":
    main()
