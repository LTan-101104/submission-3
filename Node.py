from Person import Person
from Student import Student
from Employee import Employee

class Node():
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def getData(self):
        return self.data    
    
    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def setPrevious(self, prev):
        self.prev = prev

    def getPrevious(self):
        return self.prev
    
    def __str__(self):
        return self.data.__str__()    
    
