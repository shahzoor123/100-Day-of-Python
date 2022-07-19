from Calculator_class import Calculator

print("Welcome to your own Calculator")
user_value1 = int(input("What is your 1 Number:\n"))
user_value2 = int(input("What is your 2 Number:\n"))
operation = input("What operation you want to perform:\n")

calculator = Calculator()

if operation == "+":
    print(f"Your answer is: {calculator.add(user_value1, user_value2)}")
elif operation == "-":
    print(f"Your answer is: {calculator.sub(user_value1, user_value2)}")
elif operation == "*":
    print(f"Your answer is: {calculator.mul(user_value1, user_value2)}")
elif operation == "/":
    print(f"Your answer is: {calculator.div(user_value1, user_value2)}")
