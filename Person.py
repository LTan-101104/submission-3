
class Person():
    def __init__(self, newName = "None", address = "None", phone = "999-999-9999"):
        self.newName = newName
        self.address = address
        self.phone = phone
    
    def setName(self, name):
        self.newName = name

    def getName(self):
        return self.newName

    def setPhone(self, phone):
        self.phone = phone
    
    def getPhone(self):
        return self.phone

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.getName() == other
        else: return self == other
        
    def __str__(self):
        return f"\nName    : {self.getName()}\naddress : {self.getAddress()}\nphone   : {self.getPhone()}"
    
    # def getData(self):
    #     name = input("Please enter the name for new person")
    #     address = input("Please enter the address for new person")
    #     phone = input("Please enter the phone for new person")
    #     return name, address, phone
    
    # def enterNewPerson(self):
    #     name, address, phone = self.getData()
    #     # newObj.setName(name)
    #     # newObj.setAddress(address)
    #     # newObj.setPhone(phone)
    #     user_cmd = input("Is this a student?")
    #     if user_cmd.lower() == "y": 
    #         year = int(input("Please enter Expected Graduate year"))
    #         new_obj = Student(name, address, phone, year)
    #         LinkedList.add(new_obj)
    #         return
    #     user_cmd = input("Is this an employee?")
    #     if user_cmd.lower() == "y":
    #         department = input("Please enter department")
    #         new_obj = Employee(name, address, phone, department)
    #         LinkedList.add(new_obj)
    #         return 
    #     new_obj = Person (name, address, phone)
    #     LinkedList.add(new_obj)                 

if __name__ == "__main__":
    test_subject = Person("jaime", "amherst","111-111-1111")
    print(test_subject)


