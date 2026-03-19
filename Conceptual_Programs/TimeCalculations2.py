import time

def Factorial(No) :
    fact = 1

    for i in range(1, No+1) :
        fact = fact * i
    
    return fact

def main():
    Value = int(input("Enter Number : "))

    start_time = time.time()

    Ret = Factorial(Value)

    end_time = time.time()

    print("Factorial is : ",Ret)

    print("Total execution time is : ",(end_time-start_time))
    
if __name__ == "__main__" :
    main()