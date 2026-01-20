##############################################################################################################
#   Function Name : Addition
#   Description :   It is used to addition of two numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          19/01/2026
##############################################################################################################
def Addition(No1,No2) :
    return (No1+No2)

##############################################################################################################
#   Function Name : Substraction
#   Description :   It is used to Substraction of two numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          19/01/2026
##############################################################################################################
def Substraction(No1,No2) :
    return (No1-No2)

##############################################################################################################
#   Function Name : Multiplication
#   Description :   It is used to Multiplication of two numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          19/01/2026
##############################################################################################################
def Multiplication(No1,No2) :
    return (No1*No2)

##############################################################################################################
#   Function Name : Division
#   Description :   It is used to Division of two numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          19/01/2026
##############################################################################################################
def Division(No1,No2) :
    return (No1/No2)

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main():
    Ret = 0.0
    Value1 = 0
    Value2 = 0

    print("Enter first number :")
    Value1 = int(input())

    print("Enter second number :")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)
    print("Addition is : ",Ret)

    Ret = Substraction(Value1,Value2)
    print("Substraction is : ",Ret)

    Ret = Multiplication(Value1,Value2)
    print("Multiplication is : ",Ret)

    Ret = Division(Value1,Value2)
    print("Division is : ",Ret)

##############################################################################################################
#   Starter
##############################################################################################################
if __name__ == "__main__" :
    main()