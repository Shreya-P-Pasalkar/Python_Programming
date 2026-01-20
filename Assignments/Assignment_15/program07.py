##############################################################################################################
#   Function Name : GreaterLength
#   Function Type : Lambda Function
#   Description :   It is used to check the length of string is greater than 5 or not
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
GreaterLength = lambda A : (len(A) > 5)

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Data = list()
    iSize = 0

    print("Enter number of elements you want in you list : ")
    iSize = int(input())

    for i in range(1,(iSize+1)) :
        Value = str(input())
        Data.append(Value)

    FData = list(filter(GreaterLength,Data))
    print("Filtered Data(length of string greater than 5) is : ",FData)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()