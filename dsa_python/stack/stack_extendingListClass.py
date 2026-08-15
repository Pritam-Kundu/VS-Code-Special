# Stack by extending List Class

class Stack(list):
    def is_empty(self):
        return len(self) == 0               #Object of stack also contains the properties of list class so length of self will return the length of the stack 
    def push(self, data):
        self.append(data)                   #Stack is a child class of list so we can use the properties of list class
    def pop(self):
        if not self.is_empty():
            return super().pop()            #Here we can't use self.pop because [infinite recursion will occur] self will point to the pop method in the Stack class but we wanted to point it to the pop method of list class which is parent class so we have written super.pop()...otherwise the pop method of list class was being overridden by the pop method of Stack class 
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data):            #List has an function named insert() ny using that we can insert any value at any specified index but we have to stop it so we have written another insert() method so it will be overidden and the exception will be raised
        raise AttributeError("No attribute 'insert' in Stack")
    
    
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is:",s1.peek())