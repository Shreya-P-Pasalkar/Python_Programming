#########################################################################################
# Required Header Files
#########################################################################################
import numpy as np
import math
import matplotlib.pyplot as plt

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
#   Function Name : ReLU
#   Description   : It is used to implement ReLU FUnction
#   Input         : Number
#   Output        : Result
#   Date          : 03/05/026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ReLU(Z) :
    Result = max(0,Z)

    return Result

#########################################################################################
#   Function Name : Tanh
#   Description   : It is used to implement Tanh FUnction
#   Input         : Number
#   Output        : Result
#   Date          : 03/05/026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def Tanh(Z) :
    Result = (math.exp(Z) - math.exp(-Z)) / (math.exp(Z) + math.exp(-Z))

    return Result

#########################################################################################
#   Function Name : main
#   Description   : Entry-point funtion
#   Input         : None
#   Output        : None
#   Date          : 03/05/026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def main() :
    SigmoidResults = []
    ReLUResults = []
    TanhResults = []

    #---------------------------------------------------------------------
    #   Step 1 : Inputs(X_i)
    #---------------------------------------------------------------------
    Inputs = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

    #---------------------------------------------------------------------
    #   Step 2 : Apply Activation Functions
    #---------------------------------------------------------------------
    for i in Inputs :
        Output = ReLU(i)
        ReLUResults.append(Output)

        Output = Sigmoid(i)
        SigmoidResults.append(Output)

        Output = Tanh(i)
        TanhResults.append(Output)

    #---------------------------------------------------------------------
    #   Step 3 : Display Output
    #---------------------------------------------------------------------
    plt.plot(Inputs, ReLUResults, label = "ReLU", color = "Red")
    plt.plot(Inputs, SigmoidResults, label = "Sigmoid", color = "blue")
    plt.plot(Inputs, TanhResults, label = "Tanh", color = "green")

    plt.title("Activation Functions Representation")
    plt.xlabel("Input(X)")
    plt.ylabel("Output f(X)")
    plt.grid(True)
    plt.legend()
    plt.axhline(y = 0, color = "black", linewidth = 1) # Add X-axis line
    plt.axvline(x = 0, color = "black", linewidth = 1) # Add Y-axis line
    plt.show()

    print("- "*50)
    print(("Activation functions").center(100))
    print("- "*50)

    print("ReLU = max(0, x)")
    print("Range of ReLU : 0 to infinity\n")

    print("Sigmoid = 1 / (1 + (math.exp(-Z)))")
    print("Range of Sigmoid : 0 to 1\n")

    print("Tanh = (math.exp(Z) - math.exp(-Z)) / (math.exp(Z) + math.exp(-Z))")
    print("Range of Tanh : -1 to +1\n")

    print("- "*50)

#########################################################################################
#   Starter
#########################################################################################
if __name__ == "__main__" :
    main()


