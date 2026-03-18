from functools import reduce

def CheckEven(No) :
    return (No % 2 == 0)

def Increment(No) :
    return (No + 1)

def Add(A,B) :
    return A+B

def main() :
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckEven,Data))          # filter(functionname,Data) is inbuilt function in python used to filter out the data
    print("Data after filter is :",FData)

    MData = list(map(Increment,FData))            # map(functionname,Data) is inbuilt function in python used to operate the data
    print("Data after map is :",MData)

    RData = reduce(Add,MData)                     # reduce(functionname,Data) is inbuilt function in functools library used to operate the data
    print("Data after reduce is :",RData)         

if __name__ == "__main__" :
    main() 