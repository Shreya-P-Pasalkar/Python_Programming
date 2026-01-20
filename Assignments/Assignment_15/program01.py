##############################################################################################################
#   Function Name : Square
#   Function Type : Lambda Function
#   Description :   It is used to calculate square
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
Square = lambda No : No*No

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

    MData = list(map(Square,Data))
    print("Mapped Data(Square) is : ",MData)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()