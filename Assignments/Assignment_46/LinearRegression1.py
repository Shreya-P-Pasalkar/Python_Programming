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
            "Marks" : [50,55,60,65,70]}
    
    df = pd.DataFrame(Data)

    X = df[["StudyHours"]]
    Y = df["Marks"]

    Model = LinearRegression()

    Model.fit(X,Y)

    print("Model Trained Successsfully!")

    print("Coefficient of Regression Equation (Slope) : ",Model.coef_[0])
    print("Intercept of Regression Equation (Y-Intercept) : ",Model.intercept_)


########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()