##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : RenameFileExt
#   Function Type : User-defined Function
#   Description :   Used to used to rename the extensions of a file
#   Author :        Shreya Pramod Pasalkar
#   Date :          05/02/2026
##########################################################################################################
def RenameFileExt(DirName,Ext) :
    if(os.path.exists(DirName) == False) :
        print("Directory File doesn't exists")
        return

    if(os.path.isdir(DirName) == False) :
        print(f"{DirName} is not a directory")
        return    
    
    for Foldername, SubfolderName, FileName in os.walk(DirName) :

        for fName in FileName :
            fName = os.path.join(Foldername,fName)
            if(fName.endswith(".txt")) :
                NameOnly = fName.split(".")
                name = NameOnly[0] + Ext
                fName = os.rename(fName, name)

##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    RenameFileExt(sys.argv[1],sys.argv[2])
 
##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()