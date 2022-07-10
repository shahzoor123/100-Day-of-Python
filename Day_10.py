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

def calculator():
    num1 = int(input("Enter the a number: "))
    for operators in operations:
        print(operators)   

    want_to_continue = True  
    while want_to_continue:
        which_operations = input("Pick up an operation: ")
        num2 = int(input("What the next number: "))
        calculation_function = operations[which_operations]
        answer = calculation_function(num1,num2)
        print(f"{num1} {which_operations} {num2} = {answer}")
        if input(f"Type y to continue calculating with {answer} and n to start agains ") == "y":
            num1 = answer 
        else:
            want_to_continue = False
            calculator()
            
calculator()
  

       












# fisrt solution

# if which_operations == "+":
#     answer = add(num1,num2)
# elif which_operations == "-":
#     answer = substract(num1,num2)
# elif which_operations == "*":
#     answer = add(num1,num2)
# elif which_operations == "/":
#     answer = divide(num1,num2)          


