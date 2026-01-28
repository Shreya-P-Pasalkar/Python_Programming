##############################################################################################################
#   Class Name :    Circle
#   Author :        Shreya Pramod Pasalkar
#   Date :          28/01/2026
##############################################################################################################
class Circle :
    PI = 3.14       # Class Variable

    ##########################################################################################################
    #   Function Name : __init__
    #   Function Type : special Function
    #   Description :   Constructor
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def __init__(self,) :
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    ##########################################################################################################
    #   Function Name : Accept
    #   Function Type : User Defined Function
    #   Description :   It is used to accept the radius from user
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Accept(self) :
        self.Radius = float(input("Enter Radius : "))

    ##########################################################################################################
    #   Function Name : CalculateArea
    #   Function Type : User Defined Function
    #   Description :   It is used to Calculate Area of circle
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def CalculateArea(self) :
        self.Area = self.PI * (self.Radius*self.Radius)
        return self.Area
    
    ##########################################################################################################
    #   Function Name : CalculateCircumference
    #   Function Type : User Defined Function
    #   Description :   It is used to Calculate Circumference of circle
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def CalculateCircumference(self) :
        self.Circumference = 2 * self.PI * self.Radius
        return self.Circumference
    
    ##########################################################################################################
    #   Function Name : Display
    #   Function Type : User Defined Function
    #   Description :   It is used to Display
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Display(self) :
        print("Radius : ",self.Radius)
        print("Area : ",self.Area)
        print("Circumference : ",self.Circumference)

##############################################################################################################
#   Object Creation
##############################################################################################################
obj1 = Circle()
obj2 = Circle()
obj3 = Circle()

##############################################################################################################
#   Function Calls
##############################################################################################################
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()

obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()

    

