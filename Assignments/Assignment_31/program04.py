##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : CpyDirectory
#   Function Type : User-defined Function
#   Description :   Used to used to copy files of specific extention of one directory into the other 
#   Author :        Shreya Pramod Pasalkar
#   Date :          05/02/2026
##########################################################################################################
def CpyDirectory(SrcDir,DestDir,Ext) :
    if(os.path.exists(SrcDir) == False) :
        print("Directory File doesn't exists")
        return

    if(os.path.isdir(SrcDir) == False) :
        print(f"{SrcDir} is not a directory")
        return

    if(os.path.exists(DestDir) == True and os.path.isdir(DestDir) == True) :
        print(f"{DestDir} named directory already exists")
        return
    
    os.mkdir(DestDir) 
    print(f"{DestDir} created successfully")
    
    for Foldername, SubfolderName, FileName in os.walk(SrcDir) :

        for fName in FileName :
            if(fName.endswith(Ext)) :
                SrcFilePath = os.path.join(Foldername,fName)
                DestFilePath = os.path.join(DestDir,fName)

                sobj = open(SrcFilePath, "r")
                Data = sobj.read()

                dobj = open(DestFilePath, "w") 
                dobj.write(Data)

                sobj.close()
                dobj.close()

##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    CpyDirectory(sys.argv[1],sys.argv[2],sys.argv[3])
 
##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()