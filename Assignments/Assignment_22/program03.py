##############################################################################################################
#   Class Name :    Arithmetic
#   Author :        Shreya Pramod Pasalkar
#   Date :          28/01/2026
##############################################################################################################
class Arithmetic :

    ##########################################################################################################
    #   Function Name : __init__
    #   Function Type : special Function
    #   Description :   Constructor
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def __init__(self) :
        self.Value1 = 0
        self.Value2 = 0

    ##########################################################################################################
    #   Function Name : Accept
    #   Function Type : User Defined Function
    #   Description :   It is used to accept the input from user
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Accept(self) :
        self.Value1 = int(input("Enter Value1 : "))
        self.Value2 = int(input("Enter Value2 : "))

    ##########################################################################################################
    #   Function Name : Addition
    #   Function Type : User Defined Function
    #   Description :   It is used to Calculate Addition of values
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Addition(self) :
        Add = self.Value1 + self.Value2
        return Add
    
    ##########################################################################################################
    #   Function Name : Substraction
    #   Function Type : User Defined Function
    #   Description :   It is used to Calculate Substraction of Values
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Substraction(self) :
        Sub = self.Value1 - self.Value2
        return Sub
    
    ##########################################################################################################
    #   Function Name : Multiplication
    #   Function Type : User Defined Function
    #   Description :   It is used to Calculate Multiplication of Values
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Multiplication(self) :
        Mult = self.Value1 * self.Value2
        return Mult
    
    ##########################################################################################################
    #   Function Name : Division
    #   Function Type : User Defined Function
    #   Description :   It is used to Calculate Division of Values
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Division(self) :
        Div = self.Value1 / self.Value2
        return Div
    
    ##########################################################################################################
    #   Function Name : Display
    #   Function Type : User Defined Function
    #   Description :   It is used to Display
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Display(self) :
        print("Addition : ",self.Addition())
        print("Substraction : ",self.Substraction())
        print("Multiplication : ",self.Multiplication())
        print("Division : ",self.Division())

##############################################################################################################
#   Object Creation
##############################################################################################################
obj1 = Arithmetic()
obj2 = Arithmetic()
obj3 = Arithmetic()

##############################################################################################################
#   Function Calls
##############################################################################################################
obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()
obj1.Display()

obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Multiplication()
obj2.Division()
obj2.Display()

obj3.Accept()
obj3.Addition()
obj3.Substraction()
obj3.Multiplication()
obj3.Division()
obj3.Display()

    

