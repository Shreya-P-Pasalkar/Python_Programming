from sklearn.linear_model import LinearRegression
import pandas as pd

########################################################################################
#   Function Name : main
#   Description   : Entry Point Function
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def main() :
    # Data
    Data = {"StudyHours" : [1,2,3,4,5],
            "SleepHours" : [7,6,7,6,8],
            "Marks" : [50,55,60,65,70]}
    
    df = pd.DataFrame(Data)

    X = df[["StudyHours","SleepHours"]]
    Y = df["Marks"]

    Model = LinearRegression()

    Model.fit(X,Y)

    print("Model Trained Successsfully!")

    print("Coefficients of Regression Equation (Slope) : ")
    print("Coefficient of StudyHours : ",Model.coef_[0])
    print("Coefficient of SleepHours : ",Model.coef_[1])
    print("Intercept of Regression Equation (Y-Intercept) : ",Model.intercept_)

########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()