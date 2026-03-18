def CheckEven(No) :
    return (No % 2 == 0)

def Increment(No) :
    return (No + 1)

def main() :
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckEven,Data))          # filter(functionname,Data) is inbuilt function used to filter out the data
    print("Data after filter is :",FData)

    MData = list(map(Increment,FData))            # map(functionname,Data) is inbuilt function used to operate the data
    print("Data after map is :",MData)

if __name__ == "__main__" :
    main() 