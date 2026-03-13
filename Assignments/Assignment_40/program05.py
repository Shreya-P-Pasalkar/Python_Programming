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

    AccuracyInbuilt = accuracy_score(Y_pred,Y_test)

    Y_Actual = Y_test.to_list()
    TruePositive = 0
    TrueNegative = 0
    FalsePositive = 0
    FalseNegative = 0
    i = 0

    for i in range((len(Y_Actual)-1)) :
            if((Y_Actual[i] == 1 )and (Y_pred[i] == 0)) :
                FalseNegative = FalseNegative + 1
            elif((Y_Actual[i] == 0 )and (Y_pred[i] == 0)) :
                TrueNegative = TrueNegative + 1
            elif((Y_Actual[i] == 0 )and (Y_pred[i] == 1)) :
                FalsePositive = FalsePositive + 1
            elif((Y_Actual[i] == 1) and (Y_pred[i] == 1)) :
                TruePositive = TruePositive + 1

    AccuracyX = (TruePositive + TrueNegative) / (TruePositive + TrueNegative + FalsePositive + FalseNegative)

    print("Accuracy Calculated using inbuilt function : ",AccuracyInbuilt)
    print("Accuracy Calculated manually : ",AccuracyX)

    if(AccuracyInbuilt == AccuracyX) :
        print("Verification Successfull !!")
    else :
        print("Verification Failed !!")

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()