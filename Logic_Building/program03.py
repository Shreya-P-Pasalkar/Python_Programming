################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def main() :
    i = 0
    j = 0
    Ans = 0

    # Dynammic program
    print("Enter first number : ")
    i = int(input())

    print("Enter second Number :")
    j = int(input())

    Ans = i + j

    print("Addition is : ",Ans)

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()