################################################################################
#   Function Name : CheckDivisibility
#   Description   : It is used to if number is divisible by 2
#   Input         : Number
#   Output        : boolean
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def CheckDivisibility(No) :
    
    # Iteration using for loop
    if(No % 2 == 0) :
        return True
    else :
        return False

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

    Ret = CheckDivisibility(Value)

    if(Ret == True) :
        print(f"{Value} is divisible by 2")
    else :
        print(f"{Value} is not divisible by 2")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()