##############################################################################################################
#   Required Modules
##############################################################################################################
import threading
 
##############################################################################################################
#   Function Name : ChkPrime
#   Function Type : User Defined Function
#   Description :   It is used to Check if the number is prime
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def ChkPrime(No) :
    sum = 0

    for i in range (1,No) :
        if (No%i == 0) :
            sum = sum+1
    
    if(sum == 1) :
        return True
    else :
        return False

##############################################################################################################
#   Function Name : Maximum
#   Function Type : User Defined Function
#   Description :   It is used to display Maximum element from the list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Maximum(Elements) :
    Max = 0
    for i in Elements :
        if i > Max :
            Max = i
                    
    print("Maximum Element : ",Max)
    print("--------------------------------------------------------------------------")

##############################################################################################################
#   Function Name : Minimum
#   Function Type : User Defined Function
#   Description :   It is used to display Minimum element from the list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Minimum(Elements) :
    Min = Elements[0]

    for i in Elements :
        if i < Min :
            Min = i
                    
    print("Minmum Element : ",Min)
    print("--------------------------------------------------------------------------") 

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0
    i = 0
    Data = list()

    print("Number of elements you want in list : ")
    Size = int(input())
    
    print("Enter numbers : ")
    for i in range (Size) :
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target = Maximum, args = (Data,))
    T2 = threading.Thread(target = Minimum, args = (Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")
    
###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
