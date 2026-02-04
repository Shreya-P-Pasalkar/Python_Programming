##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : CountWords
#   Function Type : User-defined Function
#   Description :   Used to count number of words in file
#   Author :        Shreya Pramod Pasalkar
#   Date :          04/02/2026
##########################################################################################################
def CountWords(File) :
    Count = 0
    
    if(os.path.exists(File) == False) :
        print(f"{File} doesn't exists")
        return
    
    fobj = open(File,"r")

    for line in fobj :
        Updated = line.split() 
        
        for word in Updated :
            Count += 1

    fobj.close()

    return Count
    
##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    Ret = CountWords(sys.argv[1])

    print("Number of words in file : ",Ret)

##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()