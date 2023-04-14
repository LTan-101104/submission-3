from Person import Person

class Student(Person):
    def __init__(self, newName="None", address="None", phone="999-999-9999", year = 9999):
        super().__init__(newName, address, phone)
        self.year = year
    
    def getGraduationYear(self):
        return self.year
    
    def setGraduationYear(self, year):
        self.year = year

    def __str__(self):
        personString = super().__str__()
        return personString + f"\nExpected Graduation Year: {self.getGraduationYear()}"
    
if __name__ == "__main__":
    test_subject = Student("TAN LE", "90 Butterfield", "413-210-4427", 2026)
    print(test_subject)
    print(test_subject.getGraduationYear())