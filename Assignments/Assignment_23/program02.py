##############################################################################################################
#   Class Name :    BankAccount
#   Author :        Shreya Pramod Pasalkar
#   Date :          28/01/2026
##############################################################################################################
class BankAccount :
    ROI = 10.5      # Class Variable

    ##########################################################################################################
    #   Function Name : __init__
    #   Function Type : special Function
    #   Description :   Constructor
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def __init__(self,A,B) :
        self.Name = A
        self.Amount = B

    ##########################################################################################################
    #   Function Name : Deposit
    #   Function Type : User Defined Function
    #   Description :   It is used to Desposit money into bank account
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Deposit(self) :
        Deposit = int(input("Enter amount to deposit : "))
        self.Amount = self.Amount + Deposit

    ##########################################################################################################
    #   Function Name : Withdraw
    #   Function Type : User Defined Function
    #   Description :   It is used to Withdraw money from bank account
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Withdraw(self) :
        Withdraw = int(input("Enter amount to Withdraw : "))
        
        if (Withdraw <= self.Amount) :
            self.Amount = self.Amount - Withdraw
        else :
            print("Insufficient Balance")

    ##########################################################################################################
    #   Function Name : CalculateInterest
    #   Function Type : User Defined Function
    #   Description :   It is used to calculate interest on balance
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def CalculateInterest(self) :
        Interest = (self.Amount * self.ROI) / 100
        return Interest

    ##########################################################################################################
    #   Function Name : Display
    #   Function Type : User Defined Function
    #   Description :   It is used to Display
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Display(self) :
        print("Account Holder Name : ",self.Name)
        print("Current Balance : ",self.Amount)
        print("Interest : ",self.CalculateInterest())

##############################################################################################################
#   Object Creation
##############################################################################################################
obj1 = BankAccount("Shreya Pramod Pasalkar",1000)
obj2 = BankAccount("Ritesh Pramod Pasalkar",2000)

##############################################################################################################
#   Function Calls
##############################################################################################################
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
obj1.Display()

obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()
obj2.Display()