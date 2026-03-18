from sklearn.preprocessing import StandardScaler

########################################################################################
#   Function Name : main
#   Description   : Entry Point Function
#   Input         : Nothing
#   Output        : Nothing
#   Date          : 18/03/2026
#   Author        : Shreya Pramod Pasalkar
########################################################################################
def main() :
    Border = "-"*70
    Data = [[25,20000], [30,40000], [35,80000]]

    print(Border)
    print("Data before Scaling :")
    print(Border)
    print(Data)
    print(Border)

    Scaler = StandardScaler()

    Data_scaled = Scaler.fit_transform(Data)

    print(Border)
    print("Data after Scaling : ")
    print(Border)
    print(Data_scaled)
    print(Border)

########################################################################################
#   Starter
########################################################################################
if __name__ == "__main__" :
    main()