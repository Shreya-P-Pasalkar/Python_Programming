import numpy as np

########################################################################################
#   Function Name : CalculateMean
#   Description   : It is used to calculate mean
#   Input         : Data
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def CalculateMean(Data) :

    Mean = np.mean(Data)
    print("Data : ")
    print(Data)
    print("Mean of Data is : ",Mean)

########################################################################################
#   Function Name : main
#   Description   : Entry Point Function
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def main() :
    Data = [6, 7, 8, 9, 10, 11, 12]

    CalculateMean(Data)

########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()