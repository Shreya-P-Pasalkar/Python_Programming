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

    Model = DecisionTreeClassifier()

    Model.fit(X_train,Y_train)

    Y_pred = Model.predict(X_test)

    Accuracy = accuracy_score(Y_pred,Y_test)

    print(f"Accuracy is : {Accuracy *100}%")

    Con_Matrix = confusion_matrix(Y_test, Y_pred)

    DisplayMatrix = ConfusionMatrixDisplay(confusion_matrix= Con_Matrix)

    DisplayMatrix.plot()

    plt.show()


#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()