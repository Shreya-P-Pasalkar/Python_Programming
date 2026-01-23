##############################################################################################################
#   Required Modules
##############################################################################################################
import threading
import concurrent.futures

##############################################################################################################
#   Function Name : Addition
#   Function Type : User Defined Function
#   Description :   It is used to return addition of elements in a list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Addition(Elements) :
    sum = 0
    for i in Elements :
        sum = sum + i
                    
    return sum

##############################################################################################################
#   Function Name : Product
#   Function Type : User Defined Function
#   Description :   It is used to return product of elements in a list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Product(Elements) :
    Mult = 1

    for i in Elements :
        Mult = Mult * i
                    
    return Mult

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

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor :
        future1 = executor.submit(Addition,Data)
        future2 = executor.submit(Product,Data)

    result1 = future1.result()
    result2 = future2.result()

    print("Addition is : ",result1)
    print("Product is : ",result2)
    
    print("Exit from main")
    
###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
