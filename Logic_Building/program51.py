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

    while(iNo != 0) :
        iDigit = iNo % 10
        iNo = iNo // 10
        print(f"Number is : {iNo}")
        print(f"Digit is : {iDigit}")
        print("--------------------------------------------------")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()
