##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : DisplayTxtFile
#   Function Type : User-defined Function
#   Description :   Used to used to display the .txt files in the directory
#   Author :        Shreya Pramod Pasalkar
#   Date :          05/02/2026
##########################################################################################################
def DisplayTxtFile(DirName) :
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
                print(fName)

##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    DisplayTxtFile(sys.argv[1])
 
##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()