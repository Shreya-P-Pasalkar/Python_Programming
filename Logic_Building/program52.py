################################################################################
#   Function Name : DisplayDigits
#   Description   : It is used to display digits
#   Input         : Number
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar   
################################################################################
def DisplayDigits(iNo) :
    iDigit = 0

    while(iNo != 0) :
        iDigit = iNo % 10
        iNo = iNo // 10
        print(f"Number is : {iNo}")
        print(f"Digit is : {iDigit}")
        print("--------------------------------------------------")

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
    iDigit = 0

    iNo = int(input("Enter Number : "))

    print(f"\nOriginal Number is : {iNo}")
    print("--------------------------------------------------")
    
    # Updater
    if(iNo < 0) :
        iNo = -iNo

    DisplayDigits(iNo)

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()
