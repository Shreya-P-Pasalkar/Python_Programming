################################################################################
#   Function Name : CheckPerfect
#   Description   : It is used to check perfect
#   Input         : Number
#   Output        : Boolean
#   Author        : Shreya Pramod Pasalkar   
################################################################################
def CheckPerfect(No) :
    Sum = 0

    # we cannot give two conditions in for loop
    # Python syntax is strictly: for item in iterable
    for i in range(1,((No/2) + 1)) :
        if(No % i == 0) :
            Sum = Sum + i

    return (Sum == No)

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

    if(No < 0) :
        No = -No

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
