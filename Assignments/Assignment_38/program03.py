#################################################################################################
#   Required Header Files
#################################################################################################
import pandas as pd

#################################################################################################
#   Function Name : Display
#   Usage : To display information about the Dataset
#   Date : 1/03/2026
#   Author : Shreya Pramod Pasalkar
#################################################################################################
def Display(df) :

    Border = "-" * 100
    Sum = 0
    Avg = 0
    Max = 0
    len = 0

    print(Border)
    
    print("Average Study Hours : ")
    for i in df['StudyHours'] :
        Sum = Sum + i
        len = len + 1
    Avg = Sum / len
    print(Avg)
    print("-"*50)

    print("Average Attendance : ")
    for i in df['Attendance'] :
        Sum = Sum + i
        len = len + 1
    Avg = Sum / len
    print(Avg)
    print("-"*50)

    print("Maximum Prevous Score : ")
    for i in df['PreviousScore'] :
        if(Max < i) :
            Max = i
    print(Max)
    print("-"*50)

    print("Maximum Sleep Hours : ")
    Max = 0
    for i in df['SleepHours'] :
        if(Max < i) :
            Max = i
    print(Max)
    print("-"*50)


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
    #   Display 
    #############################################################################################
    Display(df)

#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()

