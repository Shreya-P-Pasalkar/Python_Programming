class Demo :
    def __init__(self) :        # Contructor
        print("Inside Constructor")

    def __del__(self) :         # Destructor
        print("Inside Destructor")

obj = Demo()

print("End of Application")