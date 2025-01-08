
import sys


def addition(num1, num2):  
    p=34
    res=num1+num2
    return res

def subtraction(num1, num2):
    res=num1-num2
    return res

def multiplication(num1, num2):
     res=num1*num2
     return res

def division(num1, num2):
    res=num1/num2
    return res

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

opr = sys.argv[3]


print("Addiiton-",addition(num1,num2))
print("Subtraction-",subtraction(num1,num2))
print("Multiplication-",multiplication(num1,num2))
print("Division-",division(num1,num2))

if opr=="add":
    result=addition(num1,num2)
    print("Result=",result)