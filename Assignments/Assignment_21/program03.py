##############################################################################################################
#   Required Modules
##############################################################################################################
import threading

##############################################################################################################
#   Global Variables
##############################################################################################################
Counter = 0

##############################################################################################################
#   Function Name : Increment
#   Function Type : User Defined Function
#   Description :   It is used to increment the value
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Increment(Elements) :
    global Counter 

    for i in range(5) :
        with threading.Lock() :
            Counter = Counter + 1

##############################################################################################################
#   Function Name : Decrement
#   Function Type : User Defined Function
#   Description :   It is used to increment the value
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Decrement(Elements) :
    global Counter 

    for i in range(3) :
        with threading.Lock() :
            Counter = Counter - 1

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0
    global Counter
    
    print("Enter number : ")
    Value = int(input())

    T1 = threading.Thread(target = Increment, args = (Value,))
    T2 = threading.Thread(target = Decrement, args = (Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Shared variable value at the end : ",Counter)

    print("Exit from main")
    
###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
