################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar  
################################################################################
def main() :
    # Display Digits - static
    # Selection

    iNo = 35467
    iDigit = 0

    print(f"Original Number is : {iNo}")

    print("--------------------------------------------------")
    iDigit = iNo % 10
    iNo = iNo // 10
    print(f"Number is : {iNo}")
    print(f"Digit is : {iDigit}")
    print("--------------------------------------------------")

    iDigit = iNo % 10
    iNo = iNo // 10
    print(f"Number is : {iNo}")
    print(f"Digit is : {iDigit}")
    print("--------------------------------------------------")

    iDigit = iNo % 10
    iNo = iNo // 10
    print(f"Number is : {iNo}")
    print(f"Digit is : {iDigit}")
    print("--------------------------------------------------")

    iDigit = iNo % 10
    iNo = iNo // 10
    print(f"Number is : {iNo}")
    print(f"Digit is : {iDigit}")
    print("--------------------------------------------------")

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
