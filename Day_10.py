from ast import operator


print("calculator")



def add(n1,n2):
    return n1 + n2


def substract(n1,n2):
    return n1 - n2


def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2    

operations = {
  "+":add,
  "-":substract,
  "*" : multiply,
  "/" : divide 
   }

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for operators in operations:
    print(operators)

which_operations = input("Pick an operation from the line above: ")
# fisrt solution


# if which_operations == "+":
#     answer = add(num1,num2)
# elif which_operations == "-":
#     answer = substract(num1,num2)
# elif which_operations == "*":
#     answer = add(num1,num2)
# elif which_operations == "/":
#     answer = divide(num1,num2)          


# second solution

calculation_function = operations[which_operations]
answer = calculation_function(num1,num2)


print(f"{num1} {which_operations} {num2} = {answer}")