##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys
import hashlib

##########################################################################################################
#   Function Name : CalculateChecksum
#   Function Type : User-defined Function
#   Description :   Used to used to calculate checksum of a file 
#   Author :        Shreya Pramod Pasalkar
#   Date :          05/02/2026
##########################################################################################################
def CalculateChecksum(FileName) :
    hobj = hashlib.md5()

    fobj = open(FileName, "rb")

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0) :
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

##########################################################################################################
#   Function Name : DisplayChecksum
#   Function Type : User-defined Function
#   Description :   Used to used to display checksum of every file or a directory into a log file 
#   Author :        Shreya Pramod Pasalkar
#   Date :          05/02/2026
##########################################################################################################
def DisplayChecksum(DirName) :
    Border = "-"*70
    fobj = open("LogFile1", "w")
    fobj.write(f"{Border}\n")
    fobj.write("-------------------------Welcome to Log File!-------------------------\n")
    fobj.write(f"{Border}\n")

    if((os.path.exists(DirName) == False)) :
        print(f"{DirName} doesn't exists")
        return
    
    if(os.path.isdir(DirName) == False) :
        print(f"{DirName} is not a directory")

    for Foldername, Subfoldername, Filename in os.walk(DirName) :

        for fName in Filename :
            fName = os.path.join(Foldername,fName)
            Ret = CalculateChecksum(fName)

            fobj.write(f"Checksum of {fName} is : {Ret}\n")

    fobj.write(f"{Border}\n")
    fobj.write("------------------------------Thank You!------------------------------\n")
    fobj.write(f"{Border}\n")

##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    DisplayChecksum(sys.argv[1])
 
##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()