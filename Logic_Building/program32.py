################################################################################
#   Function Name : DisplayFactors
#   Description   : It is used to display factors of 6
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def DisplayFactors() :

    # Sequence

    if((6%1) == 0) :
        print("1")
    if((6%2) == 0) :
        print("2")
    if((6%3) == 0) :
        print("3")
    if((6%4) == 0) :
        print("4")
    if((6%5) == 0) :
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

    DisplayFactors()

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()