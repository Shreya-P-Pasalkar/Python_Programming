##############################################################################################################
#   Required Modules
##############################################################################################################
import threading

##############################################################################################################
#   Function Name : SumEven
#   Function Type : User Defined Function
#   Description :   It is used to print sum of even Elements in a list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def SumEven(Elements) :
    i = 0
    sum = 0

    for i in Elements :
            if (i%2 == 0) :
                sum = sum + i
    
    print("Sum of Even Elements is : ",sum)

##############################################################################################################
#   Function Name : SumOdd
#   Function Type : User Defined Function
#   Description :   It is used to print sum of Odd Elements in a list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def SumOdd(Elements) :
    i = 0
    sum = 0

    for i in Elements :
            if (i%2 != 0) :
                sum = sum + i
    
    print("Sum of Odd Factors is : ",sum)      

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

    T1 = threading.Thread(target = SumEven, args = (Data,))
    T2 = threading.Thread(target = SumOdd, args = (Data,))

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
