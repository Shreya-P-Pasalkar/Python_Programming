##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : CpyContent
#   Function Type : User-defined Function
#   Description :   Used to copy contents of one file into the other
#   Author :        Shreya Pramod Pasalkar
#   Date :          04/02/2026
##########################################################################################################
def CpyContent(SourceFile,DestFile) :
    if(os.path.exists(SourceFile) == False) :
        print("Source File doesn't exists")
        return
    
    fobj1 = open(SourceFile,"r")
    print("Source File Opened Successfully")

    Data = fobj1.read()

    fobj2 = open(DestFile,"w")
    print("Destination File opened successfully")

    fobj2.write(Data)

    print(f"Contents of {SourceFile} successfully copied into {DestFile}")

    fobj1.close()
    fobj2.close()

##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    CpyContent(sys.argv[1],sys.argv[2])

##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()