##############################################################################################################
#   Function Name : ChkPerfect
#   Description :   It is used to check whether the given number is perfect or not
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
def ChkPerfect(No) :
    Sum = 0

    for i in range(1,((int)(No/2)+1)) :
        if((No%i) == 0) :
            Sum = Sum + 1
     
    return (Sum == 1)
    
##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main():
    Value = 0
    Ret = 0

    print("Enter Value :")
    Value = int(input())

    Ret = ChkPerfect(Value)

    if(Ret == True) :
        print(Value," is a perfect number")
    else :
        print(Value," is not a perfect number")

##############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()