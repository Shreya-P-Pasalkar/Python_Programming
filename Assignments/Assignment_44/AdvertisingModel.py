import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

########################################################################################
#   Function Name : DisplayInfo
#   Description   : It is used to display information
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def DisplayInfo(Info) :
    Border = "="*70

    print(Border)
    print(Info)
    print(Border)

########################################################################################
#   Function Name : DataLoading
#   Description   : It is used to load the csv that is datset
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def LoadData() :
    DisplayInfo("Step 1 : Load the Data")

    df = pd.read_csv("Advertising.csv")

    print("Data Loaded Successfully!")

    return df

########################################################################################
#   Function Name : ShowData
#   Description   : It is used to display basic data from dataset
#   Input         : Dataframe object
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def ShowData(df, Msg) :
    DisplayInfo(Msg)

    print("---------------------------------------------------------------------")
    print("First 5 Rows : ")
    print(df.head())
    print("---------------------------------------------------------------------\n")

    print("---------------------------------------------------------------------")
    print("Columns in dataset : ")
    print(df.columns.tolist())
    print("---------------------------------------------------------------------\n")

    print("---------------------------------------------------------------------")
    print("Shape of Dataset : ",df.shape)
    print("---------------------------------------------------------------------\n")

    print("---------------------------------------------------------------------")
    print("Missing Values : ")
    print(df.isnull().sum())
    print("---------------------------------------------------------------------\n")

########################################################################################
#   Function Name : DataPreprocessing
#   Description   : It is used to preprocess the dataset
#   Input         : Dataframe object
#   Output        : Dataframe Object
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def DataPreprocessing(df) :
    DisplayInfo("Step 2 : Data Preproccesing")

    print("Data before dropping uneccessary columns : ")
    print("---------------------------------------------------------------------")
    print(df.head())
    print("---------------------------------------------------------------------")

    df = df.drop(df.filter(regex = "Unname").columns,axis = 1)

    print("Data After dropping uneccessary columns : ")
    print("---------------------------------------------------------------------")
    print(df.head())
    print("---------------------------------------------------------------------")

    return df

########################################################################################
#   Function Name : BuiltModel
#   Description   : It is used to train and test model
#   Input         : Dataframe object
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def BuiltModel(df) :
    # Model Training
    DisplayInfo("Step 3 : Train the Model")

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    # Train Test splitting
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state= 42)

    # Model Selection
    Model = LinearRegression()

    Model.fit(X_train, Y_train)

    print("Model Trained Successfully!")

    # Testing the Model
    DisplayInfo("Step 4 : Test the Model")

    Y_pred = Model.predict(X_test)

    print("---------------------------------------------------------------------")
    print("Actual Sales : ")
    print("---------------------------------------------------------------------")
    print(Y_test.tolist()) 
    print("---------------------------------------------------------------------\n")

    print("---------------------------------------------------------------------")
    print("Predicted Sales : ")
    print("---------------------------------------------------------------------")
    print(Y_pred.tolist()) 
    print("---------------------------------------------------------------------\n")

    DisplayMetrics(Y_pred,Y_test)

########################################################################################
#   Function Name : DisplayMetrics
#   Description   : It is used to display metrics of model
#   Input         : Predicted Y , Actual Y
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def DisplayMetrics(Y_pred, Y_test) :
    DisplayInfo("Step 5 : Metrics Display")

    print("Mean Absolute Error : ",mean_absolute_error(Y_test,Y_pred))
    print("Mean Squared Error : ",mean_squared_error(Y_test,Y_pred))
    print("R2 Score : ",r2_score(Y_test,Y_pred))

########################################################################################
#   Function Name : main
#   Description   : Entry Point Function
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def main() :
    df = LoadData()

    ShowData(df, "Initial Data")

    df = DataPreprocessing(df)

    BuiltModel(df)

    DisplayInfo("Thank you for using our Application!")


if __name__ == "__main__" :
    main()