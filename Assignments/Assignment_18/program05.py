##############################################################################################################
#   Required Module
##############################################################################################################
import MarvellousNum

##############################################################################################################
#   Function Name : ListPrime
#   Function Type : User Defined Function
#   Description :   It is used to find the Prime elements in the list and return addition of them
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def ListPrime(Elements) :
    Sum = 0
    
    for i in Elements :
        if(MarvellousNum.ChkPrime(i) == True) :
            Sum = Sum + i

    return Sum

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0
    iSize = 0
    Number = 0
    Data = list()
    Ret = 0

    print("Enter Number of elements you want in your list : ")
    iSize = int(input())

    print("Enter Elements :")

    for i in range (1,(iSize+1)) :
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)

    print("Data : ",Data)
    print("Addition of prime elements in the list : ",Ret)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
