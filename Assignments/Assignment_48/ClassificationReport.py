from sklearn.metrics import classification_report,confusion_matrix,precision_score,f1_score,recall_score,precision_recall_fscore_support

########################################################################################
#   Function Name : ClassificationReport
#   Description   : It is used to display Classification Report
#   Input         : Data
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def ClassificationReport(A, P) :
    Border = "=" * 80
    Border2 = "-" * 60

    print(Border)
    print("CONFUSION MATRICS : ")
    print(confusion_matrix(A,P))
    print(Border2)  
    print("CLASSIFICATION REPORT : ")
    print(classification_report(A,P))
    print(Border)

########################################################################################
#   Function Name : main
#   Description   : Entry Point Function
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def main() :
    Actual = [1,1,1,1,0,0,0,0]
    Predicted = [1,1,0,1,0,1,0,0]

    ClassificationReport(Actual,Predicted)

########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()