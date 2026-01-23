##############################################################################################################
#   Function Name : Multiplication
#   Function Type : Lambda Function
#   Description :   It is used to do multiplication of two numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
Multiplication = lambda No1,No2 : No1*No2

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter first Number : ")
    Value1 = int(input())

    print("Enter second Number : ")
    Value2 = int(input())

    Ret = Multiplication(Value1,Value2)

    print("Multiplication of ",Value1,"&",Value2," : ",Ret)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
