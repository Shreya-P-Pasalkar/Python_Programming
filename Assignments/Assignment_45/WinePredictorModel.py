import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

########################################################################################
#   Function Name : DisplayInfo
#   Description   : It is used to display information 
#   Input         : Information
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def DisplayInfo(Info) :
    Border = "=" * 105

    print(Border)
    print(Info)
    print(Border)

########################################################################################
#   Function Name : LoadData
#   Description   : It is used to display information 
#   Input         : Information
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def LoadData() :
    DisplayInfo("Step 1 : Load Dataset")

    df = pd.read_csv("WinePredictor.csv")

    print("Dataset loaded Successfully!")

    return df

########################################################################################
#   Function Name : ShowData
#   Description   : It is used to display data 
#   Input         : Dataframe Object, Message
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def ShowData(df, Msg) :
    DisplayInfo(Msg)

    print("------------------------------------------------------------------------")
    print("First 5 Rows of Dataset : ")
    print(df.head())
    print("------------------------------------------------------------------------\n")

    print("------------------------------------------------------------------------")
    print("Columns in the Dataset : ")
    print(df.columns.tolist())
    print("------------------------------------------------------------------------\n")

    print("------------------------------------------------------------------------")
    print("Shape of Dataset : ",df.shape)
    print("------------------------------------------------------------------------\n")

    print("------------------------------------------------------------------------")
    print("Missing values in the data : ")
    print(df.isnull().sum())
    print("------------------------------------------------------------------------\n")

########################################################################################
#   Function Name : DataPreprocessing
#   Description   : It is used to preprocess the data before using it
#   Input         : Dataframe Object
#   Output        : Dataframe Object
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def DataPreprocessing(df) :
    DisplayInfo("Step 2 : Data Preprocessing")

    print("------------------------------------------------------------------------")
    print("Data before dropping unnneccesary columns : ")
    print(df.head())
    print("------------------------------------------------------------------------")

    df = df.drop(df.filter(regex = "unname").columns)

    print("Data after dropping unnneccesary columns : ")
    print(df.head())
    print("------------------------------------------------------------------------")

    print("There are no missing values in this Dataset so no need to handle missing values")
    print("------------------------------------------------------------------------")

    print("Data Preprocessing done Successfully!")

########################################################################################
#   Function Name : BuiltModel
#   Description   : It is used to train,test and check accuracy of the Model
#   Input         : Dataframe Object
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def BuiltModel(df) :
    # Data Splitting
    DisplayInfo("Step 3 : Train Test Splitting")

    X = df.drop(columns = ["Class"]) 
    Y = df["Class"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state= 42)

    print("Data splitted successfully!")

    # Model creation
    Model = KNeighborsClassifier(n_neighbors=5)

    # Scaling Features
    DisplayInfo("Step 4 : Feature Scaling")

    Scaler = StandardScaler()

    X_train_scaled = Scaler.fit_transform(X_train)
    X_test_scaled = Scaler.fit_transform(X_test)

    print("Feature scaling done successfully!")

    # Training Model
    DisplayInfo("Step 5 : Model Training")
    Model.fit(X_train_scaled,Y_train)
    print("Model trained Successfully!")

    # Testing Model
    DisplayInfo("Step 6 : Model Testing")
    Y_pred = Model.predict(X_test_scaled)

    # Accuracy Calculation
    DisplayInfo("Step 7 : Estimating Model Performance")
    Accuracy = accuracy_score(Y_pred, Y_test)
    print(f"Accuracy of Model : {(Accuracy * 100)} %")

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

    DataPreprocessing(df)

    BuiltModel(df)

########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()