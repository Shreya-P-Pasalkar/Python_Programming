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
#   Function Name : Prime
#   Function Type : User Defined Function
#   Description :   It is used to display all Prime numbers from the list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Prime(Elements) :
    i = 0
    Ret = False
    PrimeElements = list()

    for i in Elements :
            Ret = ChkPrime(i) 

            if(Ret == True) :
                PrimeElements.append(i)
                    
    print("Prime Elements : ",PrimeElements)
    print("--------------------------------------------------------------------------")

##############################################################################################################
#   Function Name : NonPrime
#   Function Type : User Defined Function
#   Description :   It is used to display all Non Prime numbers from the list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def NonPrime(Elements) :
    i = 0
    Ret = False
    NonPrimeElements = list()

    for i in Elements :
            Ret = ChkPrime(i) 

            if(Ret == False) :
                NonPrimeElements.append(i)
                    
    print("Non Prime Elements : ",NonPrimeElements)  
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

    T1 = threading.Thread(target = Prime, args = (Data,))
    T2 = threading.Thread(target = NonPrime, args = (Data,))

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
