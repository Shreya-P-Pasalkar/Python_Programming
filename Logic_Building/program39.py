################################################################################
#   Function Name : CountNonFactors
#   Description   : It is used to count Non-factors
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def CountNonFactors(No) :
    iSum = 0

    # Handling negative Value
    if(No < 0) :
        No = -No
    
    # Iteration using for loop
    for i in range(1,(No + 1)) :
        if((No % i) != 0) :
            iSum += 1

    return iSum

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

    Ret = CountNonFactors(Value)

    print(f"Total number of non-factors of {Value} are : {Ret}")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()