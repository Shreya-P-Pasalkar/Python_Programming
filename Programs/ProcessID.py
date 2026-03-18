import os       # platform dependent module

def main():
    print("PID of running process is : ",os.getpid())
    print("PID of parent process is : ",os.getppid())

if __name__ == "__main__" :
    main()