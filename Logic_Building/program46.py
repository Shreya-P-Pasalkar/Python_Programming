################################################################################
#   Function Name : CheckPrime
#   Description   : It is used to if number is prime of not
#   Input         : Number
#   Output        : boolean
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def CheckPrime(No) :
    bFlag = True

    # Optimized
    # Time complexity : O(N/2)
    for i in range(2,(No//2)+1) :
        if((No % i) == 0) :
            bFlag = False

        if(bFlag == False) :
            break

    return bFlag


################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def main() :
    Value = 0
    Ret = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = CheckPrime(Value)

    if(Ret == True) :
        print(f"{Value} is prime")
    else :
        print(f"{Value} is not prime")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()