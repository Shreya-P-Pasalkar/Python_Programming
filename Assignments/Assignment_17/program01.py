##############################################################################################################
#   Required Module
##############################################################################################################
from Arithmetic import *

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value1 = 0
    Value2 = 0
    Result = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Result = Add(Value1,Value2)
    print("Addition is : ",Result)

    Result = Sub(Value1,Value2)
    print("Substraction is : ",Result)

    Result = Div(Value1,Value2)
    print("Division is : ",Result)

    Result = Mult(Value1,Value2)
    print("Multiplication is : ",Result)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()