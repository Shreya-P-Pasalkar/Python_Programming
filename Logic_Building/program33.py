################################################################################
#   Function Name : DisplayFactors
#   Description   : It is used to display factors
#   Input         : Number
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def DisplayFactors(No) :

    # Sequence
    # Wrong Approach ~ Static
    if((No%1) == 0) :
        print("1")
    if((No%2) == 0) :
        print("2")
    if((No%3) == 0) :
        print("3")
    if((No%4) == 0) :
        print("4")
    if((No%5) == 0) :
        print("5")

################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def main() :
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    DisplayFactors(Value)

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()