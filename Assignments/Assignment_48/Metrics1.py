import numpy as np
import math

########################################################################################
#   Function Name : CalculateMean
#   Description   : It is used to calculate mean
#   Input         : Data
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def CalculateMetrics(Data) :

    print("Data : ")
    print(Data)

    Mean = np.mean(Data)
    print("Mean of Data is : ",Mean)

    # Variance = summ(X - X_mean)^2 / N
    Numerator = 0
    Variance = 0

    for i in Data :
        Numerator = Numerator + ((i - Mean)**2)
    
    Variance = Numerator / len(Data)

    print("Variance of Data is : ",Variance)

    # Standard Deviation = sqrt(summ(X - X_mean)^2 / N)
    Std = 0

    Std = math.sqrt(Variance)

    print("Standard Deviation of Data is : ",Std)

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

    CalculateMetrics(Data)

########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()