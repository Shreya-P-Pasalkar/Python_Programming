from sklearn.preprocessing import StandardScaler
import math 

########################################################################################
#   Function Name : EuclideanDistance
#   Description   : It is used to calculate Euclidean Distance
#   Input         : Data
#   Output        : Distance
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def EuclideanDistance(Data) :
    Distance = 0

    x1, y1 = Data[0]
    x2, y2 = Data[1]

    Distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

    return Distance

########################################################################################
#   Function Name : main
#   Description   : Entry Point Function
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def main() :
    Border = "-"*80
    EucDist = 0
    Data = [[25,20000], [30,40000], [35,80000]]

    print(Border)
    print("Data before Scaling :")
    print(Border)
    print(Data)
    print(Border)

    EucDist = EuclideanDistance(Data)
    print("Euclidean Distance between 2 points before scaling : ",EucDist)
    print(Border)

    Scaler = StandardScaler()

    Data_scaled = Scaler.fit_transform(Data)

    print(Border)
    print("Data after Scaling : ")
    print(Border)
    print(Data_scaled)
    print(Border)

    EucDist = EuclideanDistance(Data_scaled)
    print("Euclidean Distance between 2 points after scaling : ",EucDist)
    print(Border)

########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()