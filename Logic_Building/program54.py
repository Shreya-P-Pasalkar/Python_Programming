################################################################################
#   Function Name : CountDigits
#   Description   : It is used to count digits
#   Input         : Number
#   Output        : Number
#   Author        : Shreya Pramod Pasalkar   
################################################################################
def CountDigits(iNo) :
    # Without taking digits
    iCount = 0

    while(iNo != 0) :
        iNo = iNo // 10

        iCount = iCount + 1

    return iCount

################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar  
################################################################################
def main() :
    # Display Digits - dynammic
    # Iteration - while loop

    iNo = 0
    iRet = 0

    iNo = int(input("Enter Number : "))

    print("\n--------------------------------------------------")
    print(f"Original Number is : {iNo}")
    
    # Updater
    if(iNo < 0) :
        iNo = -iNo

    iRet = CountDigits(iNo)

    print(f"Total Number of digits are : {iRet}")
    print("--------------------------------------------------")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()
