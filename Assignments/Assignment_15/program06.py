##############################################################################################################
#   Required modules
##############################################################################################################
from functools import reduce

##############################################################################################################
#   Function Name : Minimum
#   Function Type : User Defined Function
#   Description :   It is used to check the maximum number
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
def Minimum(No1,No2) :
    if(No1 < No2) :
        return No1
    else :
        return No2

##############################################################################################################
#   Function Name : ChkMinimum
#   Function Type : Lambda Function
#   Description :   It is used to check the maximum number
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
ChkMinimum = lambda No1,No2 : Minimum(No1,No2)

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

    RData = reduce(Minimum,Data)
    print("Reduces Data(Minimum number) is : ",RData)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()