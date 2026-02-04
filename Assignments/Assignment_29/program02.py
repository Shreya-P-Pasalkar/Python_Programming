##########################################################################################################
# Required Modules
##########################################################################################################
import os

##########################################################################################################
#   Function Name : DisplayContent
#   Function Type : User-defined Function
#   Description :   Used to display contents of file
#   Author :        Shreya Pramod Pasalkar
#   Date :          04/02/2026
##########################################################################################################
def DisplayContent(FileName) :
    if(os.path.exists(FileName) == False) :
        print("File doesn't exists")
        return
    
    fobj = open(FileName,"r")
    print("File Opened Successfully")

    Data = fobj.read()

    print("Data read from file : ",Data)

    fobj.close()
    
##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    FileName = input("Enter name of file :")

    Ret = DisplayContent(FileName)

##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()