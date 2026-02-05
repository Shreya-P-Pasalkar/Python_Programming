##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys
import hashlib
import time

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
#   Function Name : DisplayDuplicate
#   Function Type : User-defined Function
#   Description :   Used to used to display duplicate file from the directory  and delete it
#   Author :        Shreya Pramod Pasalkar
#   Date :          05/02/2026
##########################################################################################################
def DisplayDuplicate(DirName) :
    start_time = time.time()

    Border = "-"*70
    fobj = open("LogFile4", "w")
    fobj.write(f"{Border}\n")
    fobj.write("-------------------------Welcome to Log File!-------------------------\n")
    fobj.write(f"{Border}\n")

    if((os.path.exists(DirName) == False)) :
        print(f"{DirName} doesn't exists")
        return
    
    if(os.path.isdir(DirName) == False) :
        print(f"{DirName} is not a directory")

    Duplicate = {}

    for Foldername, Subfoldername, Filename in os.walk(DirName) :

        for fName in Filename :
            fName = os.path.join(Foldername,fName)

            Ret = CalculateChecksum(fName)

            Checksum = CalculateChecksum(fName) 

            if(Checksum in Duplicate) :
                Duplicate[Checksum].append(fName)
            else :
                Duplicate[Checksum] = [fName]

    Result = list(filter(lambda X : (len(X) > 1) ,Duplicate.values() ))

    cnt = 0

    for value in Result :
        fobj.write("Duplicate Files : \n")
        for subvalue in value :
            fobj.write(f"Deleted duplicate file : {subvalue}\n")
            os.remove(subvalue)
            cnt = cnt + 1
        fobj.write(f"Total deleted files : {cnt}\n")
    
    end_time = time.time()

    fobj.write(f"Time required for execution : {(end_time - start_time)}\n")

    fobj.write(f"{Border}\n")
    fobj.write("------------------------------Thank You!------------------------------\n")
    fobj.write(f"{Border}\n")
            
##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :    
    DisplayDuplicate(sys.argv[1])

##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main() 