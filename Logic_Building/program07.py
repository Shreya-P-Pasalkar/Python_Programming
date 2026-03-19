################################################################################
#   Function Name : CheckEven
#   Description   : It is used to check if the given number is even or not
#   Input         : One Number
#   Output        : boolean
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def CheckEven(No) :
    if((No % 2) == 0) :
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
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = CheckEven(Value)

    if(Ret == True) :
        print(f"{Value} is Even number")
    else :
        print(f"{Value} is not a Even Number")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()