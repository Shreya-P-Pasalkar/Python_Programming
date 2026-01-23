##############################################################################################################
#   Required Modules
##############################################################################################################
import threading
import os

##############################################################################################################
#   Function Name : ChkSmall
#   Function Type : User Defined Function
#   Description :   It is used to check and print sum of small elements in a string
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def ChkSmall(Elements) :
    i = 0
    Sum = 0

    for i in Elements :
        if (i >= 'a' and i<= 'z') :
            Sum = Sum + 1

    print("Sum of small elements is : ",Sum)

    print("Small Thread id : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    print("----------------------------------------------------------------")

##############################################################################################################
#   Function Name : ChkCapital
#   Function Type : User Defined Function
#   Description :   It is used to check and print sum of capital elements in a string
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def ChkCapital(Elements) :
    i = 0
    Sum = 0

    for i in Elements :
        if (i >= 'A' and i<= 'Z') :
            Sum = Sum + 1

    print("Sum of capital elements is : ",Sum)

    print("Capital Thread id : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    print("----------------------------------------------------------------")

##############################################################################################################
#   Function Name : ChkNumbers
#   Function Type : User Defined Function
#   Description :   It is used to check and print sum of Numeric elements in a string
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def ChkNumbers(Elements) :
    i = 0
    Sum = 0

    for i in Elements :
        if (i >= '0' and i<= '9') :
            Sum = Sum + 1

    print("Sum of numeric elements is : ",Sum)

    print("Numbers Thread id : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)

    print("----------------------------------------------------------------")
        

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Data = ""
    
    print("Enter String : ")
    Data = (input())

    Small = threading.Thread(target = ChkSmall, args = (Data,))
    Capital = threading.Thread(target = ChkCapital, args = (Data,))
    Numbers = threading.Thread(target = ChkNumbers, args = (Data,))

    Small.start()
    Small.join()

    Capital.start()
    Capital.join()

    Numbers.start()
    Numbers.join()

    print("Exit from main")
    
###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
