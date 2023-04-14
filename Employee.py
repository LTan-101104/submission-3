from Person import Person

class Employee(Person):
    def __init__(self, newName="None", address="None", phone="999-999-9999", department = "not assigned"):
        super().__init__(newName, address, phone)
        self.department = department

    def getDepartment(self):
        return self.department
    
    def setDepartment(self, department):
        self.department = department

    def __str__(self):
        personString = super().__str__()
        return personString + f"\nDepartment: {self.getDepartment()}"
    

if __name__ == "__main__":
    test_subject = Employee("Tan Le", "90 Butterfield", "413-210-4427", "CICS")
    print(test_subject)