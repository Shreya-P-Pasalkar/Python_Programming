#################################################################################################
#   Required Header Files
#################################################################################################
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

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

    print("Actual Values : ")
    print(list(Y_test))

    print("Predicted Values : ")
    print(list((Y_pred)))

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()