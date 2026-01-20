##############################################################################################################
#   Function Name : ChkOdd
#   Function Type : Lambda Function
#   Description :   It is used to check if the number is Odd or not
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
ChkOdd = lambda No : ((No%2) != 0)

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

    FData = list(filter(ChkOdd,Data))
    print("Filtered Data(Odd elements) is : ",FData)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()