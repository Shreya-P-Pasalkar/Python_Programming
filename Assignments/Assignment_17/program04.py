##############################################################################################################
#   Function Name : FactorsAddition
#   Function Type : User Defined Function
#   Description :   It is used to calculate addition of factors
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def FactorsAddition(No) :
    i = 0
    iSum = 0

    for i in range(1,No) :
        if (No%i == 0) :
            iSum = iSum + i

    return iSum

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = FactorsAddition(Value)

    print("Addition of Factors is : ",Ret)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()