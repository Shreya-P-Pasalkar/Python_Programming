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
    K = 3 

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
    print(Border)
    print("K-Nearest Neighbours are :")

    Votes = {}

    for Neighbour in SortedData[:K] :
        print(f"{Neighbour['Point']} - Distance : {Neighbour['distance']}")

        Label = Neighbour['Label']
        Votes[Label] = Votes.get(Label,0) + 1

    print(Border)

    #####################################

    print(Border)
    
    predicted_label = max(Votes)

    print("Predicted Label(Color) is : ",predicted_label)

    print(Border)

############################################################################

def main() :
    UserDefinedKNN()

if __name__ == "__main__" :
    main()