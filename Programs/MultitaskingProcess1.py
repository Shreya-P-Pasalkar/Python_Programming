import multiprocessing
import time
import os

def SumEven(No):
    print("PID of SumEven : ",os.getpid())      # 51 SumEven
    print("PPID of SumEven : ",os.getppid())    # 21 main
    sum = 0

    for i in range(2,No+1,2):
        sum = sum+i

    print("Even Sum is : ",sum)

def SumOdd(No):
    print("PID of SumOdd : ",os.getpid())       # 101 SumOdd
    print("PPID of SumEven : ",os.getppid())    # 21 main
    sum = 0

    for i in range(1,No+1,2):
        sum = sum+i

    print("Odd Sum is : ",sum)

def main():
    print("PID of main : ",os.getpid())         # 21 main
    print("PPID of main : ",os.getppid())       # 11 cmd

    start_time = time.time()
    t1 = multiprocessing.Process(target = SumEven,args = (100000000,))
    t2 = multiprocessing.Process(target = SumOdd,args = (100000000,))

    t1.start()
    t2.start()   

    t1.join()
    t2.join()

    end_time = time.time()

    print("Total time required : ",(end_time-start_time))
    
if __name__ == "__main__" :
    main()