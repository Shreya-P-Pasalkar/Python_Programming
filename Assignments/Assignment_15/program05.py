##############################################################################################################
#   Required modules
##############################################################################################################
from functools import reduce

##############################################################################################################
#   Function Name : Maximum
#   Function Type : User Defined Function
#   Description :   It is used to check the maximum number
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
def Maximum(No1,No2) :
    if(No1 > No2) :
        return No1
    else :
        return No2

##############################################################################################################
#   Function Name : ChkMaximum
#   Function Type : Lambda Function
#   Description :   It is used to check the maximum number
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
ChkMaximum = lambda No1,No2 : Maximum(No1,No2)

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Data = list()
    iSize = 0

    print("Enter number of elements you want in you list : ")
    iSize = int(input())

    for i in range(1,(iSize+1)) :
        Value = int(input())
        Data.append(Value)

    RData = reduce(ChkMaximum,Data)
    print("Reduces Data(Maximum number) is : ",RData)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()