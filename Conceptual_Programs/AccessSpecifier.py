class Demo :
    def __init__ (self) :
        # Worst way to achieve access specifier, there is no concept of access specifires in python
        self.No1 = 10       # public
        self._No2 = 20      # protected
        self.__No3 = 30     # private

obj = Demo()

print()