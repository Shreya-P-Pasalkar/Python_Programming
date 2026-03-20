################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def main() :
    Value1 = 0
    Value2 = 0

    print("Enter first Number : ")
    Value1 = int(input())

    print("Enter second Number : ")
    Value2 = int(input())

    if((Value1 % Value2) == 0) :
        print(f"{Value1} is completely divisible by {Value2}")
    else :
        print(f"{Value1} is not completely divisible by {Value2}")

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()