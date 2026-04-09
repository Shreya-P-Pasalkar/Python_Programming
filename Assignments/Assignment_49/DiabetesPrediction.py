import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

#########################################################################################
#   Function Name : DisplayStart
#   Description   : It is used to display header on console
#   Input         : Info
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DisplayStart(Info) :
    Border = "="*80

    print(Border)
    print(Info)
    print(Border)

#########################################################################################
#   Function Name : DisplayEnd
#   Description   : It is used to display header on console
#   Input         : None
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DisplayEnd() :
    Border = "="*80

    print(Border)

#########################################################################################
#   Function Name : DataLoading
#   Description   : It is used to load csv 
#   Input         : Info
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DataLoading() :
    df = pd.read_csv("diabetes.csv")

    print("Data loaded successfully!!")

    return df

#########################################################################################
#   Function Name : EDA
#   Description   : It is used to perform Exploratory Data Analysis
#   Input         : dataframe
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def EDA(df) :
    print("----------------------------------------------------------")
    print("First 5 Rows from the Data : ")
    print("----------------------------------------------------------")
    print(df.head())
    print("----------------------------------------------------------")

    #########################################################################

    print("----------------------------------------------------------")
    print("Column Info : ")
    print("----------------------------------------------------------")
    print(df.info())
    print("----------------------------------------------------------") 

    #########################################################################

    print("----------------------------------------------------------")
    print("Missing Values per column: ")
    print("----------------------------------------------------------")
    print(df.isnull().sum())
    print("----------------------------------------------------------")  

    #########################################################################

    print("----------------------------------------------------------")
    print("Statistics : ")
    print("----------------------------------------------------------")
    print(df.describe())
    print("----------------------------------------------------------") 

    #########################################################################

    print("----------------------------------------------------------")
    print("Plotting Distribution of Target Variable : ")
    print("----------------------------------------------------------")

    Colors = ["lightcoral","lightgreen"]
    Graph = sns.countplot(x= "Outcome", data=df, hue= "Outcome", palette=Colors)
    Graph.legend(labels=["0 : Diabetes Negative", "1: Diabetes Positive"],title="Test Result")
    plt.title("Class Distribution of Categorical Outcome")
    plt.show()

    print("Distribution Plotted Successfully!")
    
    print("----------------------------------------------------------")

    #########################################################################

    print("----------------------------------------------------------")
    print("Visualization : ")
    print("----------------------------------------------------------")

    Colors = ["lightcoral","lightgreen"]

    Graph = sns.boxplot(data=df, x= "Outcome", y= "Glucose", hue= "Outcome", palette=Colors)

    Graph.legend(labels=["0 : Diabetes Negative", "1: Diabetes Positive"],title="Test Result")
    plt.title("Checking Outliers using BOXPLOT")
    plt.ylabel("Glucose")
    plt.xlabel("Diabetes Result")
    plt.show()

    print("Boxplot Plotted Successfully!")

    sns.pairplot(df, hue="Outcome", palette= "husl")

    plt.title("PAIRPLOT to check distribution of features")
    plt.show()

    print("Pairplot Plotted Successfully!")
    
    print("----------------------------------------------------------")

#########################################################################################
#   Function Name : DataPreprocessing
#   Description   : It is used to perform Data Preprocessing
#   Input         : Dataframe
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DataPreprocessing(df) :
    # Checking Missing Values
    print("----------------------------------------------------------")
    print("Missing Values in Columns : ")
    print("----------------------------------------------------------")
    print(df.isnull().sum())
    print("----------------------------------------------------------")
    
    # Feature Scaling
    print("----------------------------------------------------------")
    print("Feature Scaling : ")
    print("----------------------------------------------------------")

    print("Dataframe before Scaling Features : ")
    print(df.head())

    Scaler = MinMaxScaler()

    Features = df.drop(columns=["Outcome"])

    Scaled_Features = Scaler.fit_transform(Features)

    # Put the scaled values back into the Datframe without touching the Outcome
    df[Features.columns] = Scaled_Features

    print("Dataframe after Scaling Features : ")
    print(df.head())

    print("Features Scaled successfully!!")
    print("----------------------------------------------------------")

#########################################################################################
#   Function Name : TrainTestSplit
#   Description   : It is used to split dataset into traing and testing dataset
#   Input         : Dataframe
#   Output        : X_train, X_test, Y_train, Y_test
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def TrainTestSplit(df) : 
    X = df.drop(columns=["Outcome"])
    Y = df["Outcome"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state = 42)

    print("Data splitted into Training and testing data successfully!!")

    return X_train, X_test, Y_train, Y_test

#########################################################################################
#   Function Name : ModelBuilding
#   Description   : It is used to built Machine Learning Model(KNN and Logistic Regression)
#   Input         : X_train, Y_train
#   Output        : KNNModel , LogisticModel
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ModelBuilding(X_train, Y_train) :
    # Building Model for K-Nearest-Neighbors
    KNNModel = KNeighborsClassifier()
    KNNModel.fit(X_train, Y_train)

    # Building Logistic Regression Model
    LogisticModel = LogisticRegression()
    LogisticModel.fit(X_train, Y_train)

    print("KNN Model trained successfully!!")
    print("Logistic Regression Model trained successfully!!")

    return KNNModel , LogisticModel

#########################################################################################
#   Function Name : ModelEvaluation
#   Description   : It is used to evaluate Models
#   Input         : KNNModel, LogisticModel, X_test, Y_test
#   Output        : Y_pred1, Y_pred2
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ModelEvaluation(KNNModel, LogisticModel, X_test, Y_test) :
    # KNN Model Evaluation
    print("----------------------------------------------------------")
    print("KNN Model Evaluation : ")

    Y_pred1 = KNNModel.predict(X_test)

    Report = classification_report(Y_test, Y_pred1)
    print("Classification Report KNN Model : ")
    print(Report)

    print("----------------------------------------------------------")

    # Logistic Regression Model Evaluation
    print("----------------------------------------------------------")
    print("Logistic Regression Model Evaluation : ")

    Y_pred2 = LogisticModel.predict(X_test)

    Report = classification_report(Y_test, Y_pred2)
    print("Classification Report for Logistic Regression : ")
    print(Report)

    print("----------------------------------------------------------")

    # Confusion Matric Display
    print("----------------------------------------------------------")
    print("Confusion Matric Display : ")

    # For KNN
    print("For KNN")
    cm = confusion_matrix(Y_test, Y_pred1)

    display = ConfusionMatrixDisplay(confusion_matrix= cm, display_labels= ["Negative", "Positive"])
    display.plot(cmap="Blues")
    plt.title("Confusion Matrix for KNN Model")
    plt.show()

    print("Confusion Matrix displayed sucessfully!!")

    # For Logistic Regression
    print("For Logistic Regression")
    cm = confusion_matrix(Y_test, Y_pred2)

    display = ConfusionMatrixDisplay(confusion_matrix= cm, display_labels= ["Negative", "Positive"])
    display.plot(cmap="Greens")
    plt.title("Confusion Matrix for Logistic Regression Model")
    plt.show()

    print("Confusion Matrix displayed sucessfully!!")

    print("----------------------------------------------------------")

    return Y_pred1, Y_pred2

#########################################################################################
#   Function Name : FinalOutput
#   Description   : It is used to create csv files
#   Input         : KNNdf, Logisticdf
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def FinalOutput(KNNdf, Logisticdf) :
    KNNdf.to_csv("KNNPrediction.csv")
    Logisticdf.to_csv("LogisticPrediction.csv")

    print("KNN test results csv created successfully!!")
    print("Logistic Regression test results csv created successfully!!")

#########################################################################################
#   Function Name : main
#   Description   : Entry-point funtion
#   Input         : None
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def main() :
    DisplayStart("Step 1 : Data Loading")
    # Step 1 : Loading Data(csv)
    df = DataLoading()
    DisplayEnd()

    DisplayStart("Step 2 : Exploratory Data Analysis")
    # Step 2 : Exploratory Data Analysis
    EDA(df)
    DisplayEnd()

    DisplayStart("Step 3 : Data Preprocessing")
    # Step 2 : Exploratory Data Analysis
    DataPreprocessing(df)
    DisplayEnd()

    DisplayStart("Step 4 : Splitting Training and Testing Data")
    # Step 4 : Splitting Training and Testing Data
    X_train,X_test,Y_train,Y_test = TrainTestSplit(df)
    DisplayEnd()

    DisplayStart("Step 5 : Model Building")
    # Step 5 : Model Building
    KNNModel, LogisticModel = ModelBuilding(X_train,Y_train)
    DisplayEnd()

    DisplayStart("Step 6 : Model Evaluation")
    # Step 6 : Model Evaluation
    Y_pred1, Y_pred2 = ModelEvaluation(KNNModel, LogisticModel, X_test, Y_test)
    DisplayEnd()

    DisplayStart("Step 7 : Create CSV file of Test Data")
    # Step 7 : Create CSV file of Test Data
    
    KNNdf = pd.DataFrame([[X_test],[Y_test],[Y_pred1]])
    Logisticdf = pd.DataFrame([[X_test],[Y_test],[Y_pred2]])

    FinalOutput(KNNdf, Logisticdf)
    
    DisplayEnd()

#########################################################################################
#   Starter
#########################################################################################
if __name__ == "__main__" :
    main()