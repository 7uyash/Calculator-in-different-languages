#NUMBERS ONLY

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select an option:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

input1 = int(input("Please select an operator: "))

if input1 == 1:
    print(num1 + num2)
elif input1 == 2:
    print(num1 - num2)
elif input1 == 3:
    print(num1 * num2)
elif input1 == 4:
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(num1 / num2)
