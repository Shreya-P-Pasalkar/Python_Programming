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

    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state= 42)

    Model1 = DecisionTreeClassifier(max_depth=1)
    Model2 = DecisionTreeClassifier(max_depth=4)
    Model3 = DecisionTreeClassifier(max_depth=None)

    Model1.fit(X_train,Y_train)
    Model2.fit(X_train,Y_train)
    Model3.fit(X_train,Y_train)

    Y_pred1 = Model1.predict(X_test)
    Accuracy1 = accuracy_score(Y_pred1,Y_test)
    print(f"Accuracy for max_depth 1 is : {Accuracy1 *100}%")

    Y_pred2 = Model2.predict(X_test)
    Accuracy2 = accuracy_score(Y_pred2,Y_test)
    print(f"Accuracy for max_depth 4 is : {Accuracy2 *100}%")

    Y_pred3 = Model3.predict(X_test)
    Accuracy3 = accuracy_score(Y_pred3,Y_test)
    print(f"Accuracy for max_depth none is : {Accuracy3 *100}%")

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()