class Employee:
    empCount = 0

    def __init__(self, name, id, salary, department, rank:int):
        if not isinstance(name, str):
            raise TypeError
        else:
            self.name = name
        if not isinstance(id, int):
            raise TypeError
        else:
            self.id = id

        self.salary = salary
        self.department = department
        self.rank = rank
        Employee.empCount += 1

    def printEmplDetails(self):
        print("Name: {0}\nID:{1}\nDepartment:{2}\nRank:{3}".format(self.name, self.id, self.department,
                                                                   self.rank))


emp1 = Employee('Ellen', 23443, 10000, "Finance", 1)
emp2 = Employee("Tracy", 44525, 300000, "HR", "Executive")

emp2.printEmplDetails()

print(Employee.empCount)
# print(hasattr(emp2,"rank"))

if (hasattr(emp2, "salary") == True):
    print(f"\nYes we can hack salary details. \nSalary amount is: ", getattr(emp2, "salary"))
    setattr(emp2, "salary", 100000)
    print("Adjusted salary is:", getattr(emp2, "salary"))
