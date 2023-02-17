number1 =eval(input("enter first number"))
number2 =eval(input("enter second number"))

operator=input("enter operator: ")

def add(num1,num2):
    x=num1+num2
    print(x)

def subtract(num1,num2):
    x=num1-num2
    print(x)

def divide(num1,num2):
    x=num1/num2
    print(x)

def multiply(num1,num2):
    x=num1*num2
    print(x)

if operator=="+":
    add(number1, number2)
elif operator=="-":
    subtract(number1, number2)
elif operator=="/":
    divide(number1, number2)
elif operator=="X" or operator=="x" or operator=="*":
    multiply(number1, number2)
else:
    print("invalid operator")