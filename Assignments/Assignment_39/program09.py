#################################################################################################
#   Required Header Files
#################################################################################################
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import seaborn as sns

#################################################################################################
#   Entry Point Function
#################################################################################################
def main() :
    Border = "-"*100

    #############################################################################################
    #   Dataset Loading
    #############################################################################################
    print(Border)
    print("Dataset Loaded Successfully")
    print(Border)

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    #############################################################################################
    #   Data Analysis
    #############################################################################################
    print(Border)
    print("Data Analysis")
    print(Border)

    print("Shape of dataset : ",df.shape)
    print("Column names : ",list(df.columns))
    print(Border)

    print("Missing Values (per column) ")
    print(df.isnull().sum())
    print(Border)

    print("Class Distribution (Result) : ")
    print(df["FinalResult"].value_counts())
    print(Border)

    print("Statistical Report of Dataset")
    print(df.describe())
    print(Border)

    #############################################################################################
    #   Data Visualization
    #############################################################################################
    print(Border)

    sns.histplot(df['StudyHours'],color= "pink", edgecolor= 'black')
    plt.xlabel("Study Hours")
    plt.ylabel("No of students")
    plt.show()
    print("Histogram Plotted Successfully!")

    sns.scatterplot(x = df['FinalResult'], y = df['SleepHours'], hue=df['FinalResult'])
    plt.show()
    print("Scatter Plot plotted successfully!")

    print(Border)

    #############################################################################################
    #   Train Test Split
    #############################################################################################

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state= 42)
    print("Train Test Split Done!")
    print(Border)

    #############################################################################################
    #   Model Training
    #############################################################################################
    Model = DecisionTreeClassifier()
    Model.fit(X_train,Y_train)
    print("Model Training Done!")
    print(Border)

    #############################################################################################
    #   Model Prediction
    #############################################################################################
    Y_pred = Model.predict(X_test)
    print("Model Prediction Done!")
    print(Border)

    #############################################################################################
    #   Accuracy Calculation
    #############################################################################################
    Accuracy = accuracy_score(Y_pred,Y_test)
    print(f"Accuracy is : {Accuracy *100}%")
    print(Border)

    #############################################################################################
    #   COnfusion Matrix generation
    #############################################################################################
    Con_Matrix = confusion_matrix(Y_test, Y_pred)

    DisplayMatrix = ConfusionMatrixDisplay(confusion_matrix= Con_Matrix)

    DisplayMatrix.plot()

    print("Confusion Matrix Plotted Successfully!")
    print(Border)

    #############################################################################################
    #   Model Training
    #############################################################################################
    print("Successfully concluding the Students Case Study!!!")
    print(Border)

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()