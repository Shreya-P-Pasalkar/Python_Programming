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

    X1 = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y1 = df['FinalResult']

    X_train,X_test,Y_train,Y_test = train_test_split(X1,Y1,test_size = 0.2,random_state= 42)

    Model = DecisionTreeClassifier()

    Model.fit(X_train, Y_train)

    Y_predtrain = Model.predict(X_train)
    Y_predtest = Model.predict(X_test)

    TrainingAccuracy = accuracy_score(Y_predtrain,Y_train)
    TestingAccuracy = accuracy_score(Y_predtest,Y_test)

    print("Training Accuracy : ",TestingAccuracy)
    print("Testing Accuracy : ",TrainingAccuracy)

    if(TrainingAccuracy > TestingAccuracy) :
        print("OVERFITTING occured here as Training Accuracy is very high and testing once is low")
    
#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()