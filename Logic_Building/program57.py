################################################################################
#   Function Name : CheckPerfect
#   Description   : It is used to check perfect
#   Input         : Number
#   Output        : Boolean
#   Author        : Shreya Pramod Pasalkar   
################################################################################
def CheckPerfect(No) :
    Sum = 0

    for i in range(1,No) :
        if(No % i == 0) :
            Sum = Sum + i

    if(Sum == No) :
        return True
    else :
        return False

################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar  
################################################################################
def main() :
    No = 0
    Ret = False

    No = int(input("Enter Number : "))

    Ret = CheckPerfect(No)

    if(Ret == True) :
        print(No," is perfect number")
    else :
        print(No," is not perfect number")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()
