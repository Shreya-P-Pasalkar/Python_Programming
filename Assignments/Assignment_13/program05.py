##############################################################################################################
#   Function Name : DisplayGrade
#   Description :   It is used to display grade based on marks
#   Author :        Shreya Pramod Pasalkar
#   Date :          20/01/2026
##############################################################################################################
def DisplayGrade(No) :

    if(No >= 75) :
        print("Grade : Distinction")
    elif(No >= 60) :
        print("Grade : First Class")
    elif(No >= 50) :
        print("Grade : Second Class")
    elif(No < 50) :
        print("Grade : Fail")
    else :
        print("Invalid entry of marks")

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main():
    Value = 0
    Ret = 0

    print("Enter Marks :")
    Value = int(input())

    DisplayGrade(Value)

##############################################################################################################
#   Starter
##################c############################################################################################
if __name__ == "__main__" :
    main()