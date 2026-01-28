##############################################################################################################
#   Class Name :    Numbers
#   Author :        Shreya Pramod Pasalkar
#   Date :          28/01/2026
##############################################################################################################
class Numbers :
    ROI = 10.5      # Class Variable

    ##########################################################################################################
    #   Function Name : __init__
    #   Function Type : special Function
    #   Description :   Constructor
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def __init__(self,A) :
        self.Value = A
        print("*******************************************")

    ##########################################################################################################
    #   Function Name : ChkPrime
    #   Function Type : User Defined Function
    #   Description :   It is used to Check if the number is prime
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def ChkPrime(self) :
        i = 0
        sum = 0

        for i in range (1,self.Value) :
            if ((self.Value%i) == 0) :
                sum += 1

        if (sum == 1) :
            return True
        else :
            return False

    ##########################################################################################################
    #   Function Name : Factors
    #   Function Type : User Defined Function
    #   Description :   It is used to find factors of a number
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Factors(self) :
        i = 0
        
        print("Factors : ")
        for i in range (1,self.Value) :
            if ((self.Value%i) == 0.0) :
                print(i,end = "\t")

        print("")

    ##########################################################################################################
    #   Function Name : SumFactors
    #   Function Type : User Defined Function
    #   Description :   It is used to find sum of factors
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def SumFactors(self) :
        i = 0
        sum = 0

        for i in range (1,self.Value) :
            if ((self.Value%i) == 0) :
                sum = sum + i

        return sum

    ##########################################################################################################
    #   Function Name : ChkPerfect
    #   Function Type : User Defined Function
    #   Description :   It is used to check if the number is perfect or not
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def ChkPerfect(self) :
        sum = self.SumFactors()
        if (sum == self.Value) :
            return True
        else :
            return False

##############################################################################################################
#   Object Creation & Function Calls
##############################################################################################################
obj1 = Numbers(10)

print("Number : ",obj1.Value)
ret = obj1.ChkPrime()
print("Given Number is prime : ",ret)
ret = obj1.ChkPerfect()
print("Given number is perfect : ",ret)
obj1.Factors()
ret = obj1.SumFactors()
print("Sum of factors : ",ret)

obj2 = Numbers(21)

print("Number : ",obj2.Value)
ret = obj2.ChkPrime()
print("Given Number is prime : ",ret)
ret = obj2.ChkPerfect()
print("Given number is perfect : ",ret)
obj2.Factors()
ret = obj2.SumFactors()
print("Sum of factors : ",ret)