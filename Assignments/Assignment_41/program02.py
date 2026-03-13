#   Points : [A, B, C, D]
#   X :      [1, 2, 3, 6]
#   Y :      [2, 3, 1, 5]
#   Label :  [R, R, B, B]

import numpy as np
import math

def Euclidean_Distance(Old,New) :
    Distance = math.sqrt(((New['X'] - Old['X']) **2) + ((New['Y'] - Old['Y']) **2))

    return Distance

def UserDefinedKNN() :
    Border = "-"*60

    Data = [
                {'Point' : 'A', 'X' : 1, 'Y' : 2, 'Label' : 'Red'},
                {'Point' : 'B', 'X' : 2, 'Y' : 3, 'Label' : 'Red'},
                {'Point' : 'C', 'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
                {'Point' : 'D', 'X' : 6, 'Y' : 5, 'Label' : 'Blue'},
           ]

############################################################################
    print(Border)

    X_Coor = int(input("Enter X Coordinate : "))
    Y_Coor = int(input("Enter Y Coordinate : "))

    print(Border)

    New_Point = {'X' : X_Coor, 'Y' : Y_Coor}

############################################################################
    for d in Data : 
        d['distance'] = Euclidean_Distance(d,New_Point)

############################################################################
    SortedData = sorted(Data, key = lambda i : i['distance'])
############################################################################
    K1 = 1
    K2 = 3
    K3 = 5

    ################# for K1 that is 1  #################
    Votes1 = {}

    for Neighbour in SortedData[:K1] :
        Label = Neighbour['Label']

        Votes1[Label] = Votes1.get(Label, 0) + 1

    Predicted_Label = max(Votes1)

    print(f"K = {K1} -> {Predicted_Label}")

    ################# for K2 that is 3  #################
    Votes2 = {}

    for Neighbour in SortedData[:K2] :
        Label = Neighbour['Label']

        Votes2[Label] = Votes2.get(Label, 0) + 1

    Predicted_Label = max(Votes2)

    print(f"K = {K3} -> {Predicted_Label}")

    ################# for K3 that is 5 #################
    Votes3 = {}

    for Neighbour in SortedData[:K3] :
        Label = Neighbour['Label']

        Votes3[Label] = Votes3.get(Label, 0) + 1

    Predicted_Label = max(Votes3)

    print(f"K = {K3} -> {Predicted_Label}")

    ####################################################

    print("Prediction changes when we increase the value of K becuase the algorithm explores more neighbors")

############################################################################

def main() :
    UserDefinedKNN()

if __name__ == "__main__" :
    main()