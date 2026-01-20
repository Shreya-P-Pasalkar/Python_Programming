##############################################################################################################
#   Function Name : ChkPalindrome
#   Description :   It is used to check if the number is palindrome
#   Author :        Shreya Pramod Pasalkar
#   Date :          19/01/2026
##############################################################################################################
def ChkPalindrome(No):
    original = str(No)
    reverse = ""

    for i in original :
        reverse = i+reverse

    return original == reverse       

##############################################################################################################
#   Entry Point Function
##############################################################################################################
def main():
    Ret = 0

    print("Enter number :")
    Value = int(input())

    Ret = ChkPalindrome(Value)

    if(Ret == True):
        print("It is palindrome")
    else :
        print("It is not a palindrome")

##############################################################################################################
#   Starter
##############################################################################################################
if __name__ == "__main__" :
    main()