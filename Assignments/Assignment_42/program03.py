# Implement Simple Linear Regression manually
import numpy as np
import matplotlib.pyplot as plt

def Linear_Regression() :
    Border = "-"*70

    # Dataset
    X = [1,2,3,4,5]     # Experience 
    Y = [20000,25000,30000,35000,40000]     # Salary

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
    # Prediction for given X
    ##############################################################
    print(Border)
    X_pred= int(input("Enter Experience for Salary prediction : "))

    Y_pred = (m * X_pred) + C

    print(f"Predicted Salary for {X_pred} Years Experience is : {Y_pred}")

    ##############################################################
    # Plotting Regression
    ##############################################################
    plt.plot(X,Y,label = 'Regression Line',color='g',marker= 'o')

    plt.title("Plotting Regression Line")
    plt.xlabel("Experience of an Employee")
    plt.ylabel("Predicted Salary")
    plt.legend()

    plt.show()

def main() :
    Linear_Regression()

if __name__ == "__main__" :
    main()