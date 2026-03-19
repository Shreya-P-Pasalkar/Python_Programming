################################################################################
#   Function Name : CheckEvenOdd
#   Description   : It is used to check if the given number is Even or Odd
#   Input         : One Number
#   Output        : boolean
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def CheckEvenOdd(No) :
    return ((No % 2) == 0)

################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def main() :
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = CheckEvenOdd(Value)

    if(Ret == True) :
        print(f"{Value} is Even number")
    else :
        print(f"{Value} is Odd Number")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()