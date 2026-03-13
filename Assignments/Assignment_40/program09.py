#################################################################################################
#   Required Header Files
#################################################################################################
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#################################################################################################
#   Entry Point Function
#################################################################################################
def main() :
    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    PerformanceIndex = []

    df_dict = df.to_dict()

    for i in df :
        Performance = (df['StudyHours'] * 2) + df['Attendance']
        PerformanceIndex.append(Performance)

    df['PerformanceIndex'] = Performance

    X1 = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours','PerformanceIndex']]
    Y1 = df['FinalResult']

    X_train,X_test,Y_train,Y_test = train_test_split(X1,Y1,test_size = 0.2,random_state= 42)

    Model = DecisionTreeClassifier()

    Model.fit(X_train, Y_train)

    Y_pred = Model.predict(X_test)

    Accuracy = accuracy_score(Y_pred,Y_test)

    print("Accuracy of Model with new feature PerformanceIndex : ",Accuracy)

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()