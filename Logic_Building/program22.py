# 5   4   3   2   1

################################################################################
#   Function Name : Display
#   Description   : It is used to display the 5 numbers in reverse order
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def Display() :
    # Iteration using for loop
    for i in range(5,0,-1) :
        print(i,end="\t")

    print()

################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def main() :
    Display()

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()