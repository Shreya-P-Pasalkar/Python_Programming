##############################################################################################################
#   Class Name :    BookStore
#   Author :        Shreya Pramod Pasalkar
#   Date :          28/01/2026
##############################################################################################################
class BookStore :
    NoOfBooks = 0

    ##########################################################################################################
    #   Function Name : __init__
    #   Function Type : special Function
    #   Description :   Constructor
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def __init__(self,A,B) :
        self.Name = A
        self.AuthorName = B
        BookStore.NoOfBooks += 1
    
    ##########################################################################################################
    #   Function Name : Display
    #   Function Type : User Defined Function
    #   Description :   It is used to Display
    #   Author :        Shreya Pramod Pasalkar
    #   Date :          28/01/2026
    ##########################################################################################################
    def Display(self) :
        print(f"{self.Name} by {self.AuthorName}.Number of Books : {self.NoOfBooks}")

##############################################################################################################
#   Object Creation and function call
##############################################################################################################
obj1 = BookStore("Design of UNIX","Mauris J Bach")
obj1.Display()
obj2 = BookStore("C Programming","Dennis Ritchie")
obj2.Display()
