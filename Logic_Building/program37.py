################################################################################
#   Function Name : DisplayNonFactors
#   Description   : It is used to display Non-factors
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def DisplayNonFactors(No) :
    # Handling negative Value
    if(No < 0) :
        No = -No
    
    # Iteration using for loop
    # Optimized
    for i in range(1,(No+1)) :
        if((No % i) != 0) :
            print(i)


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

    DisplayNonFactors(Value)

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()