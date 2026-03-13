#################################################################################################
#################################################################################################
#   Required Header Files
#################################################################################################
import pandas as pd

#################################################################################################
#   Function Name : Analyzer
#   Usage : To the relation between feature and traget 
#   Date : 1/03/2026
#   Author : Shreya Pramod Pasalkar
#################################################################################################
def Analyzer(df) :
    Border = "-"*100
    StudyHourAnalyzer = df.groupby('FinalResult')['StudyHours'].mean()

    AttendanceAnalyzer = df.groupby('FinalResult')['Attendance'].mean()

    print("Mean hours of study failed and passed students does : ")
    print(StudyHourAnalyzer)
    print("-"*50)

    print("Mean Attendance failed and passed students have : ")
    print(AttendanceAnalyzer)
    print("-"*50)

    print(Border)

    #  More the StudyHours the is more chance of clearing the exam
    #  Mean hours of study students did to pass woas 6.37hrs while 2.22 was mean of study hours of failed students
    #  More the attendance more is the probabilty of passing
    #  Mean Attendance of passed students is 86.6111 while mean of failed student's Attendance is 67.75

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
    #   Analyse relation between features and labels proportionality
    #############################################################################################
    Analyzer(df)

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()

