##############################################################################################################
#   Function Name : Addition
#   Function Type : Lambda Function
#   Description :   It is used to calculate the addition of two numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
Addition = lambda No1,No2 : (No1 + No2)
 
##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main():
    Value1 = 0.0
    Value2 = 0.0
    Ret = 0.0

    print("Enter First Number :")
    Value1 = int(input())

    print("Enter Second Number :")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)

    print("Addition of ",Value1," & ",Value2," is : ",Ret)

##############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()