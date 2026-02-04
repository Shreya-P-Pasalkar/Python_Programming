##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : LineCount
#   Function Type : User-defined Function
#   Description :   Used to count number of lines in a file
#   Author :        Shreya Pramod Pasalkar
#   Date :          04/02/2026
##########################################################################################################
def LineCount(File) :
    Count = 0

    if(os.path.exists(File) == False) :
        print(f"{File} doesn't exists")
        return
    
    fobj = open(File,"r")

    for line in fobj :
        Updated = line.strip() # strip() function is used remove whitespaces and newline charaters in line 
        Count = Count + 1

    fobj.close()

    return Count
    
##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    Ret = LineCount(sys.argv[1])

    print(f"Number of lines in {sys.argv[1]} is : {Ret}")

##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()