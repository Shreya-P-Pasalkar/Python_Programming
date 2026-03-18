########################################################################################
#   Function Name : ConfusionMetricsCalculation
#   Description   : It is used to calculate Confusion matrix metrics
#   Input         : Data
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def ConfusionMetricsCalculation(A, P) :
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for i in range(len(A)) :
        if(A[i] == 1 and P[i] == 1) :
            TP += 1
        elif(A[i] == 1 and P[i] == 0) :
            FN += 1
        elif(A[i] == 0 and P[i] == 1) :
            FP += 1
        elif(A[i] == 0 and P[i] == 0) :
            TN += 1

    print("Confusion Matrics values for actual and predicted values are : ")
    print("True Positives(TP) : ",TP)
    print("True Negatives(TN) : ",TN)
    print("False Positives(FP) : ",FP)
    print("False Negative(FN) : ",FN)

########################################################################################
#   Function Name : main
#   Description   : Entry Point Function
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def main() :
    Actual = [1,1,1,1,0,0,0,0]
    Predicted = [1,1,0,1,0,1,0,0]

    print("Actual Values : ",Actual)
    print("Predicted Values : ",Predicted)

    ConfusionMetricsCalculation(Actual,Predicted)
########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()