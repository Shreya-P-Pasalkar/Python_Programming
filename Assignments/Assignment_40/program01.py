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

    Importances = Model.feature_importances_

    FeatureInfo = pd.DataFrame({'Feature' : X.columns, 'Importances' : Importances})
    FeatureInfo = FeatureInfo.sort_values(by= "Importances",ascending=True)

    print(FeatureInfo)

    print("Least Importance feature :")
    print(FeatureInfo['Feature'].head(1))

    print("Most Importance feature : ")
    print(FeatureInfo['Feature'].tail(1))
    

    Model.predict(X_test)

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()