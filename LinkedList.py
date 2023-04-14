from Node import Node
from Person import Person
from Student import Student
from Employee import Employee

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def __getitem__(self, i): 
        if i >= self.size: return "index out of bound"
        tempNode = self.head
        tempInd = 0
        while (tempInd < i):
            tempNode = tempNode.getNext()
            tempInd += 1
        return tempNode.getData()

    def __iter__(self): 
        curNode = self.head
        while(curNode):
            yield curNode
            curNode = curNode.getNext()

    def length(self):
        return self.size

    def add(self, object): 
        addNode = Node(object)
        if not self.head:
            self.head = addNode
            self.tail = addNode
            self.size += 1
            return
        self.tail.setNext(addNode)
        addNode.setPrevious(self.tail)
        self.tail = self.tail.getNext()
        self.size += 1
         
    def search(self, name): 
        res = LinkedList()
        for index in range(0, self.length()):
            cur = self[index]
            if cur == name:
                res.add(cur)
        return res

    def insert(self, i, object): 
        if i > self.size or i < 0: return "Index is out of bound"
        addNode = Node(object)
        if self.length() == 0 or i == self.length():
            self.add(object)
            return #return to avoid Self.size increases again
        elif i == 0:
            addNode.setNext(self.head)
            self.head.setPrevious(addNode)
            self.head = addNode
        else:
            tempInd = 0
            tempNode = self.head
            while (tempInd < i - 1):
                tempNode = tempNode.getNext()
                tempInd += 1
            prev, next = tempNode, tempNode.getNext()
            addNode.setNext(next)
            addNode.setPrevious(prev)
            prev.setNext(addNode)
            next.setPrevious(addNode)
        self.size += 1


    def delete(self, i): 
        if i >= self.size: return "index out of bound"
        tempNode = self.head
        tempInd = 0
        while (tempInd < i):
            tempNode = tempNode.getNext()
            tempInd += 1
        prev, next = tempNode.getPrevious(), tempNode.getNext()
        #set prev and next, add condition to avoid edge cases when delete at tail or at head
        if prev: prev.setNext(next)
        if next: next.setPrevious(prev)
        #add condition to update self.head and self.tail in edge case
        if i == 0: self.head = self.head.getNext()
        elif i == self.length() - 1: self.tail = self.tail.getPrevious()
        self.size -= 1

    def __str__(self):
        res = ""
        for obj in self: 
            res += obj.__str__() + "\n"
        return res

if __name__ == "__main__":
    #This is my test for insert and delete
    obj1 = Student("TAN LE", "122 AA street", "9999999999" )
    obj2 = Person("John", "134 MM street")
    obj3 = Person("Phuc", "13 North NJ")
    obj4 = Person("Khoa", "13 14th street")
    obj5 = Employee("TAN LE", "134 MM Street")
    fake_list = LinkedList()
    fake_list.add(obj1)
    fake_list.add(obj2)
    fake_list.add(obj3)
    fake_list.add(obj4)
    fake_list.add(obj5)

    #test for inset
    fake_list.insert(0, Person("HOANG")) #insert at head
    print(fake_list)
    fake_list.insert(2, Person("David")) #insert at middle
    print(fake_list)
    fake_list.insert(7, Person("Nikolai")) #insert at tail
    print(fake_list) 
    # This will print out total 8 object above (including 3 new object that I just inserted)

    #test for delete
    fake_list.delete(0) #delete at head, now the list only has 7 object - just deleted object with name HOANG
    print(fake_list)
    fake_list.delete(6) #delete at tail, now the list only has 6 object - just deleted object with name Nikolai
    print(fake_list)
    fake_list.delete(2) #delete at middle, now the list only has 5 object - just deleted object with name John
    print(fake_list) #this will print 5 objects after deletion

    