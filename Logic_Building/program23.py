# 1   2   3   4   5

################################################################################
#   Function Name : Display
#   Description   : It is used to display the numbers
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def Display(No) :
    # Iteration using for loop
    for i in range(1,(No+1)) :
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
    Display(5)

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()