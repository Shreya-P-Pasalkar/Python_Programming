#################################################################################################
#   Required Header Files
#################################################################################################
import pandas as pd

#################################################################################################
#   Function Name : AnalyzeFinalResult
#   Usage : To analyse the FinalResult of students
#   Date : 1/03/2026
#   Author : Shreya Pramod Pasalkar
#################################################################################################
def AnalyzeFinalResult(df) :

    Border = "-" * 100
    
    print(Border)
    print("Analysing distribution of final results")
    print(Border)

    print(df['FinalResult'].value_counts())
    print("-"*50)

    # normalize attribute gives the percentage of each unique value
    Percentage = df['FinalResult'].value_counts(normalize = 'True') * 100
    print(Percentage)
    print("-"*50)

    # The Dataset is not balanced

#################################################################################################
#   Entry Point Function
#################################################################################################
def main() :
    Border = "-"*100
    print(Border)

    #############################################################################################
    #   Load the Dataset
    #############################################################################################
    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print("Dataset loaded sucessfully!")

    print(Border)

    #############################################################################################
    #   Analyse distribution of final result 
    #############################################################################################
    AnalyzeFinalResult(df)

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()

