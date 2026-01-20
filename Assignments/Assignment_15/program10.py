##############################################################################################################
#   Required modules
##############################################################################################################
from functools import reduce

##############################################################################################################
#   Function Name : Add
#   Function Type : User Defined Function
#   Description :   It is used to calculate Addition
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
def Add(No) :
    Sum = No+1
    return Sum

##############################################################################################################
#   Function Name : Elements
#   Function Type : Lambda Function
#   Description :   It is used to calculate number of elements
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
Elements = lambda No1,No2 : Add(No1)

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

    RData = reduce(Elements,Data)
    print("Reduced Data(Number of elements) is : ",RData)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()