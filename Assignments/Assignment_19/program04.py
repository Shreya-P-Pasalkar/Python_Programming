##############################################################################################################
#   Function Name : ChkEven
#   Function Type : Lambda Function
#   Description :   It is used to check if the number is even
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
ChkEven = lambda No : (No%2 == 0)

##############################################################################################################
#   Function Name : Square
#   Function Type : Lambda Function
#   Description :   It is used to square the given number
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
Square = lambda No : No*2

##############################################################################################################
#   Function Name : Addition
#   Function Type : Lambda Function
#   Description :   It is used to Add two numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
Addition = lambda No1,No2 : No1*No2

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
    Outcome = 0

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

    FData = list(filterX(ChkEven,Data))
    print("List after filter : ",FData)

    MData = list(mapX(Square,FData))
    print("List after map : ",MData)

    RData = reduceX(Addition,MData)
    print("Reduced Data : ",RData)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
