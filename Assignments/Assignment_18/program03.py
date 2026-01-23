##############################################################################################################
#   Function Name : Minimum
#   Function Type : User Defined Function
#   Description :   It is used to find the Minimum element from the list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Minimum(Elements) :
    iMin = 0
    
    for i in Elements :
        if(i<iMin) :
            iMin = i

    return iMin

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0
    iSize = 0
    Data = list()
    Ret = 0

    print("Enter Number of elements you want in your list : ")
    iSize = int(input())

    print("Enter Elements :")

    for i in range (1,(iSize+1)) :
        Value = int(input())
        Data.append(Value)

    Ret = Minimum(Data)

    print("Data : ",Data)
    print("Minimum element from the list : ",Ret)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
