#################################################################################################
#   Required Header Files
#################################################################################################
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

#################################################################################################
#   Entry Point Function
#################################################################################################
def main() :
    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    X1 = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y1 = df['FinalResult']

    X_train,X_test,Y_train,Y_test = train_test_split(X1,Y1,test_size = 0.2,random_state= 42)

    Model1 = DecisionTreeClassifier()

    Model1.fit(X_train,Y_train)

    Y_pred = Model1.predict(X_test)

    Accuracy1 = accuracy_score(Y_pred,Y_test)
    print(f"Accuracy of Model with StudyHours : {Accuracy1}%")

    X2 = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted']]
    Y2 = df['FinalResult']

    X_train,X_test,Y_train,Y_test = train_test_split(X2,Y2,test_size = 0.2,random_state= 42)

    Model2 = DecisionTreeClassifier()

    Model2.fit(X_train,Y_train)

    Y_pred = Model2.predict(X_test)

    Accuracy2 = accuracy_score(Y_pred,Y_test)
    print(f"Accuracy of Model with StudyHours : {Accuracy1}%")

    if Accuracy1 != Accuracy2 :
        print("Removing feature StudyHours affects the Model's Performance")
    else :
        print("Removing feature StudyHours does not affect the Model's Performance")

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()