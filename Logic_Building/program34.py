################################################################################
#   Function Name : DisplayFactors
#   Description   : It is used to display factors
#   Input         : Number
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def DisplayFactors(No) :

    # Iteration using for loop
    for i in range(1,(No+1)) :
        if((No % i) == 0) :
            print(i)

    # Time COmplexity : O(N)

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