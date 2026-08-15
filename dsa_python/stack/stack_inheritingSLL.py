# Importing module containing singly linked list
# Then defining class Stack and extending the class SLL

from linked_list.singly_linked_list import *

class Stack(SLL):
    def __init__(self):
        super().__init__()              # In python the constructor of parent class is not automatically initialized like C++ or Java so we have to explicitly initialize it 
        self.item_count = 0
    
    def is_empty(self):
        return super().is_empty()
    
    def push(self, data):
        self.insert_at_first(data)
        self.item_count += 1
        
    def pop(self):
        if not self.is_empty():
            item = self.start.data
            self.delete_first()
            self.item_count -= 1
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
print("Top element:",s1.peek())
s1.pop()
print("Top element:",s1.peek())

