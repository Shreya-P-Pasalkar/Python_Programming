##############################################################################################################
#   Required Modules
##############################################################################################################
import threading

##############################################################################################################
#   Function Name : SumEvenFactors
#   Function Type : User Defined Function
#   Description :   It is used to print sum of even factors of a number
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def SumEvenFactors(No) :
    i = 0
    sum = 0

    for i in range (1,(No+1)) :
        if (No%i == 0) :
            if (i%2 == 0) :
                sum = sum + i
    
    print("Sum of Even Factors is : ",sum)

##############################################################################################################
#   Function Name : SumOddFactors
#   Function Type : User Defined Function
#   Description :   It is used to print sum of Odd factors of a number
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def SumOddFactors(No) :
    i = 0
    sum = 0

    for i in range (1,(No+1)) :
        if (No%i == 0) :
            if (i%2 != 0) :
                sum = sum + i
    
    print("Sum of Odd Factors is : ",sum)      

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0

    print("Enter number : ")
    Value = int(input())

    EvenFactors = threading.Thread(target = SumEvenFactors, args = (Value,))
    OddFactors = threading.Thread(target = SumOddFactors, args = (Value,))

    EvenFactors.start()
    OddFactors.start()

    EvenFactors.join()
    OddFactors.join()

    print("Exit from main")
    
###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
