import numpy as np
def my_mult_operation(a,b,operation):
    if operation == "plus":
        a=a+b
    elif operation == "minus":
        a=a-b
    elif operation == "mult":
        a=a*b
    elif operation == "div":
        a=a/b
    elif operation == "pow":
        a=a**b
    return (a)
a= np.array([1,2,3,4])
b= np.array([5,6,7,8])
operation = input("Enter the operation to perform = ")
c=my_mult_operation(a,b,operation)
print(c)