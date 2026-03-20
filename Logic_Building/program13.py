################################################################################
#   Function Name : Display
#   Description   : It is used to display for N times
#   Input         : Number
#   Output        : Nothin
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def Display(No) :

    # Iteration ~ for loop using range
    for i in range(No) :
        print("Jay Ganesh...")

################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def main() :
    print("Enter Frequency : ")
    Frequency = int(input())

    Display(Frequency)

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()