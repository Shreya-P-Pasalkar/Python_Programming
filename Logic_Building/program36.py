################################################################################
#   Function Name : DisplayFactors
#   Description   : It is used to display factors
#   Input         : Number
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def DisplayFactors(No) :
    # Handling negative Value
    if(No < 0) :
        No = -No

    Dest = No // 2      # Floor Division
    
    # Iteration using for loop
    # Optimized
    for i in range(1,(Dest+1)) :
        if((No % i) == 0) :
            print(i)

    # Time Complexity : O(N/2)

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