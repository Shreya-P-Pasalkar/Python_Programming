##############################################################################################################
#   Function Name : Maximum
#   Function Type : Lambda Function
#   Description :   It is used to return maximum number among the two
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
def Maximum(A,B) :
    if(A>B):
        return A
    else :
        return B

##############################################################################################################
#   Function Name : ChkMaximum
#   Function Type : Lambda Function
#   Description :   It is used to check maximum number among the three
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
ChkMaximum = lambda No1,No2,No3 : Maximum(No1, Maximum(No2,No3))
 
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

    print("Enter Third Number :")
    Value3 = int(input())

    Ret = ChkMaximum(Value1,Value2,Value3)

    print("Maximum among the three numbers is : ",Ret)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main() 