#########################################################################################
# Required Header Files
#########################################################################################
import math

#########################################################################################
#   Function Name : Sigmoid
#   Description   : It is used to implement Sigmoid FUnction
#   Input         : Number
#   Output        : Result
#   Date          : 03/05/026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def Sigmoid(Z) :
    Result =  1 / (1 + (math.exp(-Z)))

    return Result

#########################################################################################
#   Function Name : CalculateBCE
#   Description   : It is used to implement Binary Cross Entropy
#   Input         : Actual_Outputs, Predicted_Outputs
#   Output        : Result
#   Date          : 03/05/026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def CalculateBCE(Actual_Outputs, Predicted_Outputs) :
    Summ = 0
    N = len(Actual_Outputs)
    Calculated_BCE = 0

    for i in range(N) :
        Result = Actual_Outputs[i]*math.log(Predicted_Outputs[i]) + (1 - Actual_Outputs[i])*math.log(1 - Predicted_Outputs[i])
        Summ = Summ + Result

    Calculated_BCE = -(Summ / N)
    return Calculated_BCE

#########################################################################################
#   Function Name : CalculateMSE
#   Description   : It is used to Calculate Mean Squared Error
#   Input         : Actual_Outputs, Predicted_Outputs
#   Output        : Result
#   Date          : 03/05/026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def CalculateMSE(Actual_Outputs, Predicted_Outputs) :
    N = len(Actual_Outputs)
    Summ = 0
    Calculated_MSE = 0

    for i in range(N) : 
        Result = (Actual_Outputs[i] - Predicted_Outputs[i]) ** 2
        Summ = Summ + Result

    Calculated_MSE = Summ / N
    return Calculated_MSE

#########################################################################################
#   Function Name : main
#   Description   : Entry-point funtion
#   Input         : None
#   Output        : None
#   Date          : 03/05/026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def main() :
    #---------------------------------------------------------------------
    #   Step 1 : Outpus
    #---------------------------------------------------------------------
    Actual_Outputs1 = [10,20,13,42,12,10,9.30,20,15]
    Predicted_Outputs1 = [10,20,13,42,12,10,9.30,20,15]

    Actual_Outputs2 = [1,1,1,0,1,0,0,1,1,0]
    Predicted_Outputs2 = [0.8,0.9,0.6,0.3,0.7,0.2,0.5,0.7,0.8,0.25]

    #---------------------------------------------------------------------
    #   Step 2 : Apply Loss Functions
    #---------------------------------------------------------------------
    MSE = CalculateMSE(Actual_Outputs1, Predicted_Outputs1)
    BCE = CalculateBCE(Actual_Outputs2, Predicted_Outputs2)

    #---------------------------------------------------------------------
    #   Step 3 : Display Output
    #---------------------------------------------------------------------
    print("- "*50)
    print(("~ LOSS FUNCTIONS ~").center(100))
    print("- "*50)

    print("\n1. Mean Squared Error")
    print("Mean Squared Error is a loss function measuring the average difference between predicted and actual values\n")
    print("Actual Values : ",Actual_Outputs1)
    print("Predicted Values : ",Predicted_Outputs1)
    print("Calculated Mean Squared Error : ",MSE)
    print()

    print("-" * 100)

    print("2. Binary Cross Entropy")
    print("Binary Cross-Entropy (BCE) loss, or Log Loss, measures the performance of a classification model where predictions are probabilities between 0 and 1.\n")
    print("Actual Values : ",Actual_Outputs2)
    print("Predicted Values : ",Predicted_Outputs2)
    print("Calculated Binary Cross Entropy : ",BCE)
    print()

    print("Binary Cross-Entropy Loss (Log Loss): Used for binary classification")
    print("Mean Squared Error (MSE) / L2 Loss: Used for Regression")

    print("- "*50)

#########################################################################################
#   Starter
#########################################################################################
if __name__ == "__main__" :
    main()


