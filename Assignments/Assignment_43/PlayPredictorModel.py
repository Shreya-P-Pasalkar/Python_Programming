import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#########################################################################################
#   Function Name : DisplayInfo
#   Description   : It is used to display basic info on console
#   Input         : Information to display
#   Output        : None
#   Date          : 17/03/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DisplayInfo(Info) :
    Border = "=" * 70

    print(Border)
    print(Info)
    print(Border)

#########################################################################################
#   Function Name : ShowData
#   Description   : It is used to display Dataframe to understand basic dataset 
#   Input         : Dataframe
#   Output        : None
#   Date          : 17/03/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ShowData(df,Message) :
    DisplayInfo(Message)

    print("--------------------------------------------------------------")
    print("------------------First 5 Rows of the Dataset-----------------")
    print(df.head())
    print("--------------------------------------------------------------\n")

    print("--------------------------------------------------------------")
    print("--------------------Shape of the Dataset----------------------")
    print(df.shape)
    print("--------------------------------------------------------------\n")

    print("--------------------------------------------------------------")
    print("-------------------Columns in the Dataset---------------------")
    print(df.columns.tolist())
    print("--------------------------------------------------------------\n")

    print("--------------------------------------------------------------\n")
    print("---------------Missing values from the dataset----------------")
    print(df.isnull().sum())
    print("--------------------------------------------------------------\n")

########################################################################################
#   Function Name : DataPreprocessing
#   Description   : It is used to process the data to make it training ready
#   Input         : Dataframe
#   Output        : Processed Dataframe
#   Date          : 17/03/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DataPreprocessing(df) :
    DisplayInfo("Step 2 : Preprocessing of the Dataset")

    # Removing Uneccessary Columns
    print("--------------------------------------------------------------")
    print("Column to be dropped : ")    # Unamed Column
    df = df.drop(df.filter(regex = 'Unname').columns, axis = 1)
    print("Column dropped successfully!!")
    print("Remaining columns : ")
    print(df.columns.tolist())
    print("--------------------------------------------------------------\n")

    # Encoding Columns(Label encoding)
    # Encoding columns Whether,Temperature
    print("--------------------------------------------------------------")
    print("Data before encoding : ")
    print(df.head())
    print("--------------------------------------------------------------\n")

    df['Whether'] = LabelEncoder().fit_transform(df['Whether'])
    df['Temperature'] = LabelEncoder().fit_transform(df['Temperature'])

    print("--------------------------------------------------------------")
    print("Data After Encoding : ")
    print(df.head())
    print("--------------------------------------------------------------\n")

    print("Data Preprocessed Successfully!!!")

    return(df)

########################################################################################
#   Function Name : ModelTesting
#   Description   : It is used to train the model from the datset
#   Input         : Dataframe
#   Output        : Model
#   Date          : 17/03/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ModelTesting(df) :
    DisplayInfo("Step 3 : Training Model")

    X = df[['Whether', 'Temperature']]
    Y = df['Play']

    Model = KNeighborsClassifier(n_neighbors=3)

    Model.fit(X,Y)

    print("Model Trained Successully!!!")

    DisplayInfo("Step 4 : Testing Model")

    print("Enter Whether for Testing(Overcast : 0 or Rainy : 1 or Sunny : 2 ) : ")
    W_test = int(input())

    print("Enter Temperature for Testing(Cool : 0 or Sunny : 1 or Mild : 2 ) : ")
    T_test = int(input())

    #when you get the warning with list of list you should crete df
    X_test = pd.DataFrame([[W_test, T_test]], columns=['Whether', 'Temperature'])   

    Y_pred = Model.predict(X_test)

    print("Prediction to play : ",Y_pred[0])

########################################################################################
#   Function Name : CheckAccuracy
#   Description   : It is used to train the model from the datset
#   Input         : Dataframe
#   Output        : Model
#   Date          : 17/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def CheckAccuracy(df) :
    DisplayInfo("Step 5 : Accuracy of the Model")
    X = df[["Whether", "Temperature"]]
    Y = df["Play"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 42)

    Model = KNeighborsClassifier()

    Model.fit(X_train,Y_train)

    Y_pred = Model.predict(X_test)

    Accuracy = accuracy_score(Y_pred, Y_test)

    print("Model Accuracy : ",Accuracy)

#########################################################################################
#   Function Name : main
#   Description   : Start of the Application(Entry point function)
#   Input         : None
#   Output        : None
#   Date          : 17/03/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def main() :
    DisplayInfo("Step 1 : Loading the Dataset")
    df = pd.read_csv("PlayPredictor.csv")

    print("Data loaded successfully!!!")

    ShowData(df,"Initial Data :")

    df = DataPreprocessing(df)

    ModelTesting(df)

    CheckAccuracy(df)

    DisplayInfo("Thank you for using our application!!")

if __name__ == "__main__" :
    main()