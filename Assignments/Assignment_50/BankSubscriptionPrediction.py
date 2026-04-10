import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, ConfusionMatrixDisplay, RocCurveDisplay

#########################################################################################
#   Function Name : DisplayStart
#   Description   : It is used to display header
#   Input         : Info
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar 
#########################################################################################
def DisplayStart(Info) :
    Border = "="*100

    print(Border)
    print(Info)
    print(Border)

#########################################################################################
#   Function Name : DisplayEnd
#   Description   : It is used to display header (at the end)
#   Input         : None
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DisplayEnd() :
    Border = "="*100

    print(Border,"\n")

#########################################################################################
#   Function Name : LoadDataset
#   Description   : It is used to load dataset 
#   Input         : None
#   Output        : Dataframe
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def LoadDataset() :
    df = pd.read_csv("bank-full.csv")

    print("\nDataset Loaded Successfully!\n")

    return df 

#########################################################################################
#   Function Name : EDA
#   Description   : It is used to perform Exploratory Data Analysis
#   Input         : Dataframe
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def EDA(df) :
    Border = "-"*90

    ############################################################################

    # First 5 rows of the Dataset
    print(Border)
    print("First 5 rows of the Dataset : ")
    print(Border)
    print(df.head())
    print(Border,"\n")

    ############################################################################

    # Columns (Independent and Dependent Variables)
    print(Border)
    print("Columns (Independent and Dependent Variables) : ")
    print(Border)
    print(df.columns.tolist())
    print(Border,"\n")

    ############################################################################

    # Statistics of Dataset
    print(Border)
    print("Statistics of Dataset : ")
    print(Border)
    print(df.describe())
    print(Border,"\n")

    ############################################################################
    # Missing Values
    print(Border)
    print("Missing Values per column : ")
    print(Border)
    print(df.isnull().sum())
    print(Border,"\n")

    ############################################################################

    # Visualization 
    print(Border)
    print("Visualization : ")
    print(Border)

    color = ["pink","lightgreen"]
    
    #Countplot
    sns.countplot(x= "y", data= df, hue="y", palette= color)
    plt.legend(labels= ["yes : Subscribed","no : Not Subscribed"],title= "Subscription Results")
    plt.title("COUNT_PLOT for Bank Subscription Prediction")
    plt.show()
    print("Count-Plot plotted successfully!")

    # Scatterplot
    sns.scatterplot(x="y",y="balance", data=df, hue = "y", palette= color)
    plt.legend(labels= ["yes : Subscribed","no : Not Subscribed"],title= "Subscription Results")
    plt.title("SCATTER_PLOT for Bank Subscription Prediction")
    plt.show()
    print("Scatter-Plot plotted successfully!")

    # Boxplot
    sns.boxplot(x="y", y="balance", data=df, hue = "y", palette= color)
    plt.legend(labels= ["yes : Subscribed","no : Not Subscribed"],title= "Subscription Results")
    plt.title("BOX_PLOT for Bank Subscription Prediction")
    plt.show()
    print("Box-Plot plotted successfully!")

    print(Border,"\n")

#########################################################################################
#   Function Name : DataPreprocessing
#   Description   : It is used to perform Data Preprocessing(Encoding and Scaling)
#   Input         : Dataframe
#   Output        : Dataframe
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DataPreprocessing(df) :
    Border = "-"*90

    ############################################################################
    
    # Encoding Categorical Variables
    # Using One-Hot Encoding
    # One-Hot encoding creates a new column for every unique category
    print(Border)
    print("Encoding for Categorical Variables : ")
    print(Border)

    print("Data before encoding categorical variables : ")
    print(df.head())

    df_encoded = pd.get_dummies(df, columns=["default","job","marital","education","housing","loan","contact","month","poutcome"])
    print("\nData After Encoding : ")
    print(df_encoded.head())

    print("\nTotal Columns before encoding : ")
    print(df.columns.tolist())
    print("\nTotal Columns after encoding : ")
    print(df_encoded.columns.tolist())

    ############################################################################

    df = df_encoded

    ############################################################################
    
    # Scaling Features 
    # Using Standard Scaler
    print(Border)
    print("Feature Scaling : ")
    print(Border)

    Features = df.drop(columns="y")
    Scaler = StandardScaler()
    Features_Scaled = Scaler.fit_transform(Features)

    print("Dataframe before scaling : ")
    print(df.head())
    
    df[Features.columns] = Features_Scaled

    print("\nDataset after Scaling : ")
    print(df.head())

    print()
    print(Border)
    print("Data preprocessing done successfully!")

    ############################################################################
    return df

#########################################################################################
#   Function Name : DataSplitting
#   Description   : It is used to split dataset into training and testing data
#   Input         : Dataframe
#   Output        : X_train, X_test, Y_train, Y_test
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DataSplitting(df) :
    X = df.drop(columns= "y")
    Y = df["y"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state= 42)

    print("\nData splitted into training and testing data sucessfully!\n")

    return X_train, X_test, Y_train, Y_test

#########################################################################################
#   Function Name : ModelBuilding
#   Description   : It is used to train and build Machine Learning Models
#   Input         : X_train, Y_train
#   Output        : Model
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ModelBuilding(X_train, Y_train) :
    print()

    # Logistic Regression Model
    LogisticModel = LogisticRegression()
    LogisticModel.fit(X_train,Y_train)
    print("Logistic Model built successfully!")
    
    # K_Nearest_Neighbors Classifier Model
    KNNModel = KNeighborsClassifier(n_neighbors= 5)
    KNNModel.fit(X_train, Y_train)
    print("KNeighborsClassifier Model built successfully!")

    # Random_Forest Classifier Model
    RFModel = RandomForestClassifier(n_estimators= 100, random_state= 42)
    RFModel.fit(X_train, Y_train)
    print("RandomForestClassifier Model built successfully!\n")

    return LogisticModel, KNNModel, RFModel
    
#########################################################################################
#   Function Name : ModelEvaluation
#   Description   : It is used to evaluate Machine Learning Models
#   Input         : LogisticModel, KNNModel, RFModel, X_test, Y_test
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ModelEvaluation(LogisticModel, KNNModel, RFModel, X_test, Y_test) :
    Border = "-"*90

    ############################################################################
    # Testing
    Y_pred1 = LogisticModel.predict(X_test)
    Y_pred2 = KNNModel.predict(X_test)
    Y_pred3 = RFModel.predict(X_test)

    print(Border)
    print("Model Testing done successfully!")
    print(Border)

    ############################################################################
    # Accuracy Calculation 

    print()
    print(Border)
    print("Accuaracy Calculation : ")
    print(Border)

    # For Logistic Regression 
    Accuracy1 = accuracy_score(Y_test, Y_pred1)
    print("\nLogistic Regression Model : ",Accuracy1)

    # For KNN
    Accuracy2 = accuracy_score(Y_test, Y_pred2)
    print("KNN Classifier Model : ",Accuracy2)

    # For Random Forest
    Accuracy3 = accuracy_score(Y_test, Y_pred3)
    print("Random Forest Classifier Model : ",Accuracy3,"\n")

    ############################################################################
    # Confusion Matrix Calculation 

    print(Border)
    print("Confusion Matrix : ")
    print(Border)

    # For Logistic Regression 
    cm1 = confusion_matrix(Y_test, Y_pred1)
    print("\nLogistic Regression Model : ")
    print(cm1)

    # For KNN
    cm2 = confusion_matrix(Y_test, Y_pred2)
    print("KNN Classifier Model : ")
    print(cm2)

    # For Random Forest
    cm3 = confusion_matrix(Y_test, Y_pred3)
    print("Random Forest Classifier Model : ")
    print(f"{cm3}\n")

    ############################################################################
    #  Classification Report 

    print(Border)
    print("Classification Report  : ")
    print(Border)

    # For Logistic Regression 
    cr1 = classification_report(Y_test, Y_pred1)
    print("\nLogistic Regression Model : ")
    print(cr1)
    print("------------------------------------------------------------------")

    # For KNN
    cr2 = classification_report(Y_test, Y_pred2)
    print("KNN Classifier Model : ")
    print(cr2)
    print("------------------------------------------------------------------")

    # For Random Forest
    cr3 = classification_report(Y_test, Y_pred3)
    print("Random Forest Classifier Model : ")
    print(f"{cr3}\n")

    ############################################################################
    #  ROC-AUC Score

    print(Border)
    print("ROC-AUC Score  : ")
    print(Border)

    # For Logistic Regression 
    Y_probs1 = LogisticModel.predict_proba(X_test)[:,1]
    raScore1 = roc_auc_score(Y_test, Y_probs1)
    print("\nLogistic Regression Model : ",raScore1)

    # For KNN
    Y_probs2 = KNNModel.predict_proba(X_test)[:,1]
    raScore2 = roc_auc_score(Y_test, Y_probs2)
    print("KNN Classifier Model : ",raScore2)

    # For Random Forest
    Y_probs3 = RFModel.predict_proba(X_test)[:,1]
    raScore3 = roc_auc_score(Y_test, Y_probs3)
    print("Random Forest Classifier Model : ",raScore3)

    ############################################################################
    # Visualize Results
    ############################################################################

    print(Border)
    print("Visualize Results  : ")
    print(Border)
    
    ############################################################################

    # Confusion Matrix Display

    print("Confusion Matrix Display  : ")
    print(Border)

    # For Logistic Regression 
    Display = ConfusionMatrixDisplay(confusion_matrix= cm1, display_labels=["no : Not Subscribed", "yes : Subscribed"])
    Display.plot(cmap= "Blues")
    plt.title("Confusion Matrix for Logistic Regression")
    plt.show()
    print("Confusion Matrix for Logistic Regression displayed successfully!")

    # For KNN
    Display = ConfusionMatrixDisplay(confusion_matrix= cm2, display_labels=["no : Not Subscribed", "yes : Subscribed"])
    Display.plot(cmap= "Greens")
    plt.title("Confusion Matrix for KNN Classifier")
    plt.show()
    print("Confusion Matrix for KNN Classifier displayed successfully!")

    # For Random Forest
    Display = ConfusionMatrixDisplay(confusion_matrix= cm2, display_labels=["no : Not Subscribed", "yes : Subscribed"])
    Display.plot(cmap= "plasma")
    plt.title("Confusion Matrix for Random Forest Classifier")
    plt.show()
    print("Confusion Matrix for Random Forest Classifier displayed successfully!")

    ############################################################################

    # ROC Curve Display
    print(Border)
    print("ROC Curve Display  : ")
    print(Border)

    # For Logistic Regression 
    RocCurveDisplay.from_predictions(y_true=Y_test, y_score=Y_probs1, pos_label="yes")
    plt.title("ROC Curve for Logistic Regression")
    plt.show()
    print("ROC Curve for Logistic Regression displayed successfully!")

    # For KNN
    RocCurveDisplay.from_predictions(y_true=Y_test, y_score=Y_probs2, pos_label="yes")
    plt.title("ROC Curve for KNN Classifier")
    plt.show()
    print("ROC Curve for KNN Classifier displayed successfully!")

    # For Random Forest
    RocCurveDisplay.from_predictions(y_true=Y_test, y_score=Y_probs3, pos_label="yes")
    plt.title("ROC Curve for Random Forest Classifier")
    plt.show()
    print("ROC Curve for Random Forest Classifier displayed successfully!")


    

#########################################################################################
#   Function Name : main
#   Description   : Entry-point funtion
#   Input         : None
#   Output        : None
#   Date          : 04/4/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def main() :
    # Step 1 : Load Dataset
    DisplayStart("Step 1 : Load Dataset")
    df = LoadDataset()
    DisplayEnd()

    # Step 2 : Exploratory Data Analysis
    DisplayStart("Step 2 : Exploratory Data Analysis")
    EDA(df)
    DisplayEnd()

    # Step 3 : Data Preprocessing
    DisplayStart("Step 3 : Data Preprocessing")
    df = DataPreprocessing(df)
    DisplayEnd()

    # Step 4 : Splitting Data into Training and Testing Data
    DisplayStart("Step 4 : Splitting Data into Training and Testing Data")
    X_train, X_test, Y_train, Y_test = DataSplitting(df)
    DisplayEnd()

    # Step 5 : Models Building
    DisplayStart("Step 5 : Models Building")
    LogisticModel, KNNModel, RFModel = ModelBuilding(X_train, Y_train)
    DisplayEnd()

    # Step 6 : Model Evaluation
    DisplayStart("Step 6 : Model Evaluation")
    ModelEvaluation(LogisticModel, KNNModel, RFModel, X_test, Y_test)
    DisplayEnd()

    # Application completed
    DisplayStart("Thank for using our application!")

#########################################################################################
#   Starter
#########################################################################################
if __name__ == "__main__" :
    main()
