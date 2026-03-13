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

    Model = DecisionTreeClassifier()

    Model.fit(X_train,Y_train) 

    Y_pred = Model.predict(X_test)

    Y_actual = Y_test.tolist()
    X_actual = X_train.to_dict(orient = 'index')
    iMisclassified = 0

    for i in range(len(Y_pred) - 1) :
        if(Y_pred[i] != Y_actual[i]) :
            print(X_actual[i])
            iMisclassified += 1

    print("Number of Misclassified Students : ",iMisclassified)

    if(iMisclassified == 0) :
        print("No misclassifiaction observed!")

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()