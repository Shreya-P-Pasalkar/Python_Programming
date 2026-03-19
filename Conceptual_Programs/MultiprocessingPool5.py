import os
import time
import multiprocessing

def SumCube(No):
    Sum = 0

    print("Process is running with PID : ",os.getpid())

    for i in range(1,(No+1)):
        Sum = Sum + (i**3)      

    return Sum

def main() :
    Data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    Result = []

    Start_time = time.time()

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumCube,Data)

    pobj.close()
    pobj.join()
    
    End_time = time.time()

    print(Result)
    print("Total time required : ",End_time-Start_time)

if __name__ == "__main__":
    main()