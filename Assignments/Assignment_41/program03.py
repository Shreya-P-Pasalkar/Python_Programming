#   StudyHours :  [2,  5,  6,  1]
#   Attendance :  [60, 80, 85, 50]
#   Result :      [F,  P,  P,  F]

import numpy as np
import math

def Euclidean_Distance(Old,New) :
    Distance = math.sqrt(((New['X'] - Old['StudyHours']) **2) + ((New['Y'] - Old['Attendance']) **2))

    return Distance

def UserDefinedKNN() :
    Border = "-"*60

    Data = [
                {'StudyHours' : 2, 'Attendance' : 60, 'Result' : 'Fail'},
                {'StudyHours' : 5, 'Attendance' : 80, 'Result' : 'Pass'},
                {'StudyHours' : 6, 'Attendance' : 85, 'Result' : 'Pass'},
                {'StudyHours' : 1, 'Attendance' : 50, 'Result' : 'Fail'},
           ]

############################################################################
    print(Border)

    X_Coor = int(input("Enter Study Hours : "))
    Y_Coor = int(input("Enter Attendance (0-100) : "))

    print(Border)

    New_Point = {'X' : X_Coor, 'Y' : Y_Coor}

############################################################################
    for d in Data : 
        d['distance'] = Euclidean_Distance(d,New_Point)

############################################################################
    SortedData = sorted(Data, key = lambda i : i['distance'])
############################################################################
    K = 3
    Votes = {}

    for Neighbour in SortedData[:K] :
        Label = Neighbour['Result']

        Votes[Label] = Votes.get(Label, 0) + 1

    Predicted_Label = max(Votes)

    print(f"K = {K} -> {Predicted_Label}")


############################################################################

def main() :
    UserDefinedKNN()

if __name__ == "__main__" :
    main()