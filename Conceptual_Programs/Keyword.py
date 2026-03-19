def EmployeeInfo(Name, Age, Salary, City) :
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", Salary)
    print("City : ", City)

def main() :
    # Positional
    #EmployeeInfo("Rahul", 25, 2000.50, "Pune")      # Correct
    #print(**********************************************************)
    #EmployeeInfo(25, "Rahul", "Pune", 2000.50)      # Wrong

    # Keyword
    EmployeeInfo(Age=25, Name="Rahul", City="Pune", Salary=2000.50)

if __name__ == "__main__" :
    main()