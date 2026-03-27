################################################################################
#   Function Name : CheckDivisibility
#   Description   : It is used to if number is divisible by number
#   Input         : Number
#   Output        : boolean
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def CheckDivisibility(No1,No2) :
    
    # Iteration using for loop
    if(No1 % No2 == 0) :
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
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    Ret = CheckDivisibility(Value1,Value2)

    if(Ret == True) :
        print(f"{Value1} is divisible by {Value2}")
    else :
        print(f"{Value1} is not divisible by {Value2}")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()