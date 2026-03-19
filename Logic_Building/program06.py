################################################################################
#   Function Name : Addition
#   Description   : It is used to do addition of two numbers and convert to 
#                   positive if negative
#   Input         : Two Numbers
#   Output        : Addition
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def Addition(No1,No2) :
    Ans = 0

    if(No1 < 0) :
        No1 = -No1

    if(No2 < 0) :
        No2 = -No2
        
    Ans = No1 + No2     # Business Logic
    return Ans

################################################################################
#   Function Name : main
#   Description   : Starting point of application
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Shreya Pramod Pasalkar
#   Data          : 20/03/2026         
################################################################################
def main() :
    Ret = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second Number :")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)

    print("Addition is : ",Ret)

################################################################################
#   Starter        
################################################################################
if __name__ == "__main__" :
    main()