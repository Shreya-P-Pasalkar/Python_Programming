##############################################################################################################
#   Function Name : SeventytoNinety
#   Function Type : Lambda Function
#   Description :   It is used to check if the number is in range 70-90
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
SeventytoNinety = lambda No : No>=70 and No<=90

##############################################################################################################
#   Function Name : Increment
#   Function Type : Lambda Function
#   Description :   It is used to increment number by 10
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
Increment = lambda No : No+10

##############################################################################################################
#   Function Name : Product
#   Function Type : Lambda Function
#   Description :   It is used to multiply two numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
Product = lambda No1,No2 : No1*No2

##############################################################################################################
#   Function Name : filterX
#   Function Type : User Defined Function
#   Description :   It is used to filter out the elements using specific task
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def filterX(Task,Elements) :
    i = 0
    Result = list()
    Outcome = 0.0

    for i in Elements :
        Outcome = Task(i)

        if (Outcome == True) :
            Result.append(i)

    return Result

##############################################################################################################
#   Function Name : mapX
#   Function Type : User Defined Function
#   Description :   It is used to map(operate) each element in the list
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def mapX(Task,Elements) :
    i = 0
    Result = list()

    for i in Elements :
        Outcome = Task(i)
        Result.append(Outcome)

    return Result

##############################################################################################################
#   Function Name : reduceX
#   Function Type : User Defined Function
#   Description :   It is used to reduce the list to one single output
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def reduceX(Task,Elements) :
    i = 0
    Outcome = 1

    for i in Elements :
        Outcome = Task(Outcome,i)

    return Outcome

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main() :
    Value = 0
    iSize = 0
    Data = list()

    print("Enter Number of elements you want in your list : ")
    iSize = int(input())

    print("Enter Elements :")

    for i in range (1,(iSize+1)) :
        Value = int(input())
        Data.append(Value)

    FData = list(filterX(SeventytoNinety,Data))
    print("List after filter : ",FData)

    MData = list(mapX(Increment,FData))
    print("List after map : ",MData)

    RData = reduceX(Product,MData)
    print("Reduced Data : ",RData)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
