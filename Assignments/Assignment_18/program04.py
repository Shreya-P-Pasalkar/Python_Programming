##############################################################################################################
#   Function Name : Frequency
#   Function Type : User Defined Function
#   Description :   It is used to find the Frequency of element in the list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Frequency(Elements,No) :
    iFreq = 0
    
    for i in Elements :
        if(i == No) :
            iFreq = iFreq + 1

    return iFreq

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

    print("Enter number whose frequency is to be found : ")
    Number = int(input())

    Ret = Frequency(Data,Number)

    print("Data : ",Data)
    print("Frequency of element in the list : ",Ret)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
