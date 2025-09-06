class Person( object ):
    def __init__(self, nm, id):
        self.name = nm
        self.idnumber = id

    def display(self):
        print("Name: ", self.name)
        print("ID number: ", self.idnumber)

class Employee(Person):
    def __init__(self, nam, idnum, salary, pos):
        self.salary = salary
        self.post = pos

        Person.__init__(self, nam, idnum)

a = Employee("Alexander", 20240815, 25000, "Fulltime employee")

a.display()
print()