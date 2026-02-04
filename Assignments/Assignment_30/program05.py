##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : ChkWord
#   Function Type : User-defined Function
#   Description :   Used to used to check if the give in word is present or not
#   Author :        Shreya Pramod Pasalkar
#   Date :          04/02/2026
##########################################################################################################
def ChkWord(File, String) :
    Count = 0
    
    if(os.path.exists(File) == False) :
        print(f"{File} doesn't exists")
        return
    
    fobj = open(File,"r")

    for line in fobj :
        Updated = line.split() 
        
        for word in Updated :
            if(word == String) :
                Count += 1

    fobj.close()

    if(Count > 0) :
        return True
    else :
        return False
    
##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    Ret = ChkWord(sys.argv[1],sys.argv[2])

    if(Ret == True) :
        print(f"Word {sys.argv[2]} is present")
    else :
        print(f"Word {sys.argv[2]} is not present")
 
##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()