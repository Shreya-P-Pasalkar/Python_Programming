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

    TestingData = {'StudyHours' : [2,8,5,4,2.5],'Attendance' : [75,60,60,70,30],'PreviousScore' : [60,80,60,85,50],'AssignmentsCompleted' : [2,5,6,7,4],'SleepHours' : [8,4,5,6,9]}

    df2 = pd.DataFrame(TestingData)

    Y_pred = Model1.predict(df2)
    
    df2['PredictedResult'] = Y_pred

    print(df2)

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()