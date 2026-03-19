import gc 

class Demo :
    def __init__(self) :        # Contructor
        print("Inside Constructor")

    def __del__(self) :         # Destructor
        print("Inside Destructor")

# Allocate
obj = Demo()

# Use

# Deallocate
del obj             # like free()

gc.collect()        # like System.gc()

print("End of Application")