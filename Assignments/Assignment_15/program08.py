##############################################################################################################
#   Function Name : Divisbility
#   Function Type : Lambda Function
#   Description :   It is used to check if the number is divisible by both 3 and 5
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
Divisbility = lambda No : (((No%3) == 0) and ((No%5) == 0))

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

    FData = list(filter(Divisbility,Data))
    print("Filtered Data (Divisible by 3 and 5) is : ",FData)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()