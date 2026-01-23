##############################################################################################################
#   Function Name : ElementsAddition
#   Function Type : User Defined Function
#   Description :   It is used to cdo addition of elements in list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def ElementsAddition(Elements) :
    iSum = 0
    
    for i in Elements :
        iSum = iSum + i

    return iSum

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

    for i in range (1,(iSize+1)) :
        Value = int(input())
        Data.append(Value)

    Ret = ElementsAddition(Data)

    print("Data : ",Data)
    print("Addition of elements in list : ",Ret)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
