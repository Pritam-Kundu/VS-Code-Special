# Stack using Singly Linked List Concept

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0
    
    def is_empty(self):
        return self.start == None
    
    def push(self, data):
        n = Node(data)
        n.next = self.start
        self.start = n
        self.item_count += 1            #When an element will be inserted then item_count wil be increased by 1 
    
    def pop(self):
        if not self.is_empty():
            item = self.start.data
            self.start = self.start.next
            self.item_count -= 1        #When an element will be deleted then item_count wil be decreased by 1
            return item
        else:
            raise IndexError("Stack is empty")    
    
    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return self.item_count
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)        
print("Total number of elements:",s1.size())
print("Top element is:",s1.peek())
print("Deleted element is:",s1.pop())
print("Total number of elements:",s1.size())
print("Top element is:",s1.peek())
  