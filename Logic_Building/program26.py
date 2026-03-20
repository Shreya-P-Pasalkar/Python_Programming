# 5   4   3   2   1   0   

################################################################################
#   Function Name : Display
#   Description   : It is used to display the N numbers in reverse order
#                   (Dynamically)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def Display(No) :
    # Iteration using for loop
    for i in range(No,-1,-1) :
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
    print("Enter Frequency : ")
    Freq = int(input())

    Display(Freq)

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()