##############################################################################################################
#   Function Name : ChkPrime
#   Function Type : User Defined Function
#   Description :   It is used to check if the give number is prime of not
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def ChkPrime(No) :
    i = 0
    iSum = 0

    for i in range(1,No) :
        if (No%i == 0) :
            iSum = iSum + i

    return (iSum == 1)

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = ChkPrime(Value)

    if (Ret == True) :
        print("It is a Prime Number")
    else :
        print("It is not a Prime Number")

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()