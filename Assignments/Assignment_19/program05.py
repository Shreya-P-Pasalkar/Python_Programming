##############################################################################################################
#   Function Name : ChkPrime
#   Function Type : User Defined Function
#   Description :   It is used to check if the number is prime
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def ChkPrime(No) :
    sum = 0

    for i in range (1,No) :
        if(No%i == 0) :
            sum = sum + 1

    return (sum == 1)

##############################################################################################################
#   Function Name : Multiply
#   Function Type : Lambda Function
#   Description :   It is used to Multiply the given number with 2
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
Multiply = lambda No : No*2

##############################################################################################################
#   Function Name : Maximum
#   Function Type : User Defined Function
#   Description :   It is used to return the maximum number
#   Author :        Shreya Pramod Pasalkar
#   Date :          23/01/2026
##############################################################################################################
def Maximum(No1,No2) : 
    Max = No1

    if(No1 < No2) :
        Max = No2

    return Max

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

    FData = list(filterX(ChkPrime,Data))
    print("List after filter : ",FData)

    MData = list(mapX(Multiply,FData))
    print("List after map : ",MData)

    RData = reduceX(Maximum,MData)
    print("Reduced Data : ",RData)

###############################################################################################################
#   Starter
###############################################################################################################
if __name__ == "__main__" :
    main()
