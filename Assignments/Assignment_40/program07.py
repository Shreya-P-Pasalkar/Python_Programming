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

    Model1 = DecisionTreeClassifier(random_state= 0)
    Model2 = DecisionTreeClassifier(random_state= 10)
    Model3 = DecisionTreeClassifier(random_state= 42)

    Model1.fit(X_train,Y_train) 
    Model2.fit(X_train,Y_train) 
    Model3.fit(X_train,Y_train) 

    Y_pred1 = Model1.predict(X_test)
    Y_pred2 = Model2.predict(X_test)
    Y_pred3 = Model3.predict(X_test)

    Accuracy1 = accuracy_score(Y_pred1, Y_test)
    Accuracy2 = accuracy_score(Y_pred2, Y_test)
    Accuracy3 = accuracy_score(Y_pred3, Y_test)

    if(Accuracy1 == Accuracy2 == Accuracy3) :
        print("Accuracies for all models trained using random_state as 0,10,42 is same!")
    elif(Accuracy1 != Accuracy2 != Accuracy3) :
        if(Accuracy1 > Accuracy2 > Accuracy3) :
            print("Accuracy of model with random_state 0 is greater than rest two models with random_states 10 and 42")
        elif(Accuracy1 < Accuracy2 < Accuracy3) :
            print("Accuracy of model with random_state 42 is greater than rest two models with random_states 0 and 10")
        elif(Accuracy1 < Accuracy2 > Accuracy3) :
            print("Accuracy of model with random_state 10 is greater than rest two models with random_states 0 and 42")


#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()