##############################################################################################################
#   Function Name : ChkDivisibility
#   Description :   It is used to check whether the number is divisible by 3 or not 
#   Author :        Shreya Pramod Pasalkar
#   Date :          19/01/2026
##############################################################################################################
def ChkDivisibility(No):
    Div = (No % 3)

    if (Div == 0) :
        return True
    else :
        return False

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main():
    Ans = 0.0

    print("Enter first number :")
    Value = int(input())

    Ans = ChkDivisibility(Value)

    if(Ans == True) :
        print(Value," is divisible by 3")
    else :
        print(Value," is not divisible by 3")

##############################################################################################################
#   Starter
##############################################################################################################
if __name__ == "__main__" :
    main()