################################################################################
#   Function Name : DigitSum
#   Description   : It is used to add digits
#   Input         : Number
#   Output        : Number
#   Author        : Shreya Pramod Pasalkar   
################################################################################
def DigitSum(iNo) :
    iDigit = 0
    iSum = 0

    while(iNo != 0) :
        iDigit = iNo % 10
        iNo = iNo // 10

        iSum = iSum + iDigit

    return iSum

################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar  
################################################################################
def main() :
    iNo = 0

    iNo = int(input("Enter Number : "))

    print("\n--------------------------------------------------")    
    print(f"Original Number is : {iNo}")
    
    # Updater
    if(iNo < 0) :
        iNo = -iNo

    iRet = DigitSum(iNo)

    print(f"Sum of all digits : {iRet}")
    print("--------------------------------------------------")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()
