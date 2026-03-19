##############################################################################################################
#   Function Name : EvenElements
#   Function Type : Lambda Function
#   Description :   It is used to check if the number is even
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
EvenElements = lambda No : ((No%2) == 0)

##############################################################################################################
#   Function Name : Square
#   Function Type : Lambda Function
#   Description :   It is used to calculate square of a number
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
Square = lambda No : (No*No)

##############################################################################################################
#   Function Name : NumberofElements
#   Function Type : Lambda Function
#   Description :   It is used to calculate total number of elements
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
NumberofElements = lambda A,B : A+1

##############################################################################################################
#   Function Name : FilterX
#   Function Type : User Defined Function
#   Description :   It is used to filter out the elements
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
def FilterX(Task,Elements) :
    Result = list()
    Outcome = 0.0

    for i in Elements :
        Outcome = Task(i)

        if(Outcome == True) :
            Result.append(i)

    return Result

##############################################################################################################
#   Function Name : MapX
#   Function Type : User Defined Function
#   Description :   It is used to operate elements in a list
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
############################################################################################################## 
def MapX(Task,Elements) :
    Result = list()
    Outcome = 0.0

    for i in Elements :
        Outcome = Task(i)
        Result.append(Outcome)

    return Result

##############################################################################################################
#   Function Name : ReduceX
#   Function Type : User Defined Function
#   Description :   It is used to get the desired one value result from the list
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
def ReduceX(Task,Elements) :
    Result = 0

    for i in Elements :
        Result = Task(Result,i)

    return Result

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main():
    Data = list()
    iSize = 0

    print("Enter number of elements you want in list :")
    iSize = int(input())
    
    print("Enter elements :")
    for i in range(1,(iSize+1)) :
        Value = int(input())
        Data.append(Value)

    print("Entered Elements : ",Data)

    FData = list(FilterX(EvenElements,Data))
    print("Filtered Even Elements : ",FData)

    MData = list(MapX(Square,Data))
    print("Mapped squared Elements : ",MData)

    RData = ReduceX(NumberofElements,Data)
    print("Reduced no of elements : ",RData)

###############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__":
    main()