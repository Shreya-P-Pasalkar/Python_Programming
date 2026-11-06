################################################################################
#   Function Name : CheckPerfect
#   Description   : It is used to check perfect
#   Input         : Number
#   Output        : Boolean
#   Author        : Shreya Pramod Pasalkar   
################################################################################
def CheckPerfect(No) :
    Sum = 0
    i = 1

    # Alternative to give 2 conditions
    # But in this case dual condition fails 
    while i <= (No/2) and (No % i == 0) :
        Sum = Sum + i
        i += 1

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
