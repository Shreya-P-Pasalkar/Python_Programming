##############################################################################################################
#   Function Name : Maximum
#   Function Type : Lambda Function
#   Description :   It is used to find the maximum number
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
Maximum = lambda No1,No2 : (No1 > No2)
 
##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main():
    Value1 = 0.0
    Value2 = 0.0
    Ret = False

    print("Enter First Number :")
    Value1 = int(input())

    print("Enter Second Number :")
    Value2 = int(input())

    Ret = Maximum(Value1,Value2)

    if (Ret == True) :
        print("Maximum among the two numbers is :",Value1)
    else :
        print("Maximum among the two numbers is :",Value2)

##############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()