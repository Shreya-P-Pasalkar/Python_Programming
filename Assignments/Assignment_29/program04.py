##########################################################################################################
# Required Modules
##########################################################################################################
import os
import sys

##########################################################################################################
#   Function Name : ChkContents
#   Function Type : User-defined Function
#   Description :   Used to chck if contents of two file is same or not
#   Author :        Shreya Pramod Pasalkar
#   Date :          04/02/2026
##########################################################################################################
def ChkContents(File1,File2) :
    if(os.path.exists(File1) == False) :
        print(f"{File1} doesn't exists")
        return
    
    if(os.path.exists(File2) == False) :
        print(f"{File2} doesn't exists")
        return
    
    fobj1 = open(File1, "r")
    fobj2 = open(File2, "r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if(Data1 == Data2) :
        return True
    else : 
        return False

##########################################################################################################
# Entry Point Function (User defined)
##########################################################################################################
def main() :
    Ret = ChkContents(sys.argv[1],sys.argv[2])

    if (Ret == True) :
        print("Success!")
        print("This indicates both file contents are same")
    else :
        print("Failure!")
        print("This indicates both file contents are not same")

##########################################################################################################
# Starter
##########################################################################################################
if __name__ == "__main__" :
    main()