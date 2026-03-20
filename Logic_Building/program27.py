# 2   4   6   8   10 

################################################################################
#   Function Name : Display
#   Description   : It is used to display the numbers at the diff of 2
#                   (Dynamically)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def Display(No) :
    # Iteration using for loop
    for i in range(2,(No+1),2) :
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