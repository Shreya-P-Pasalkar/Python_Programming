# Implement Simple Linear Regression manually
import numpy as np

def Linear_Regression() :
    Border = "-"*70

    # Dataset
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print(Border)
    print("Implementation of Simple Linear Regression")
    print(Border)

    ##############################################################
    # Mean Calculations 
    ##############################################################
    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    print(Border)
    print("Mean of X : ",X_mean)
    print("Mean of Y : ",Y_mean)
    print(Border)

    ##############################################################
    # Slope Calculations 
    # m = sum((x-x_mean)(y-y_mean)) / sum((x-x_mean)^2)
    ##############################################################
    m = 0
    Numerator = 0
    Denominator = 0

    for i in range(len(X)) :
        Numerator = Numerator + ((X[i] - X_mean)*(Y[i] - Y_mean))
        Denominator = Denominator + ((X[i] - X_mean)**2)

    m = Numerator / Denominator

    print(Border)
    print("Slope (m) : ",m)
    print(Border)

    ##############################################################
    # Intercept Calculations 
    # Y_mean = m*(X_mean) + C
    # C = Y_mean - m*(X_mean)
    ##############################################################
    C = 0

    C = Y_mean - (m * X_mean)

    print(Border)
    print("Intercept (C) : ",C)
    print(Border)

    ##############################################################
    # Regression Equation 
    # Y = mX + C
    ##############################################################
    print(Border)
    print("Regression Equation : ")
    print(f"Y = {m}X + {C}")
    print(Border)

    ##############################################################
    # Predicting all Y values using equation
    ##############################################################
    Y_pred = []

    for i in X :
        y = (m * i) + C
        Y_pred.append(y)

    print(Border)
    print("------------------")
    print("X    Y   Y_pred")
    print("------------------")

    for i in range(len(Y_pred) - 1) :
        print(f"{X[i]}     {Y[i]}     {Y_pred[i]}")

    print(Border)

    ##############################################################
    # Calculations for Mean Squared Error
    # MSE = sum(Y-Y_pred) / n
    ##############################################################
    n = len(X)
    Numerator = 0
    MSE = 0

    for i in range(n) :
        Numerator = Numerator + ((Y[i] - Y_pred[i])**2)

    MSE = Numerator / n

    print(Border)
    print("Mean Squared Error : ",MSE)
    print(Border)

    ##############################################################
    # Calculations for R^2 Score
    # R2Score = 1 - ((sum((Y-Y_pred)**2))  /  (sum((Y[i]) - Y_mean)**2))
    ##############################################################
    R2Score = 0
    Denominator = 0

    for i in Y :
        Denominator = Denominator + ((i - Y_mean)**2)

    R2Score = Numerator / Denominator

    print(Border)
    print("R2 Score : ",R2Score)
    print(Border)

##################################################################33333

def main() :
    Linear_Regression()

if __name__ == "__main__" :
    main()