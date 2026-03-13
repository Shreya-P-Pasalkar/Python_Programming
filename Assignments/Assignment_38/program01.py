#################################################################################################
#   Required Header Files
#################################################################################################
import pandas as pd

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
    #   Display Dataset Basic Info
    #############################################################################################
    print("First 5 records of the Dataset : \n")
    print(df.head())
    print(Border)

    print("\nLast 5 records of the Dataset :\n")
    print(df.tail())
    print(Border)

    print("Total Number of Rows and Columns : \n")
    print(df.shape)
    print(Border)

    print("List of Column Names with their Datatypes: \n")
    print(list(df.columns))
    print(Border)

    print("Datatypes of each Column : \n")
    print(df.dtypes)
    print(Border)


#################################################################################################
#   Starter
#################################################################################################
if __name__ == "__main__" :
    main()

