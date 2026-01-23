##############################################################################################################
#   Function Name : DigitsAddition
#   Function Type : User Defined Function
#   Description :   It is used to cdo addition of digits in a number
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def DigitsAddition(No) :
    digit = 0
    iSum = 0

    while (No != 0) :
        digit = int(No % 10)
        iSum = iSum + digit
        No = int(No/10)

    return iSum

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0
    Ret = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = DigitsAddition(Value)

    print("Addition of Digits : ",Ret)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
