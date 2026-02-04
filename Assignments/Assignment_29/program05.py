##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : Frequency
#   Function Type : User-defined Function
#   Description :   Used to check frequency of string in a file
#   Author :        Shreya Pramod Pasalkar
#   Date :          04/02/2026
##########################################################################################################
def Frequency(File,string) :
    Count = 0

    if(os.path.exists(File) == False) :
        print(f"{File} doesn't exists")
        return
    
    fobj = open(File,"r")

    content = fobj.read()

    Data = content.split()

    for word in Data :
        if(word == string) :
            Count = Count + 1

    fobj.close()

    return Count
    
##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    Ret = Frequency(sys.argv[1],sys.argv[2])

    print(f"Frequency of {sys.argv[2]} in {sys.argv[1]} is : {Ret}")

##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()