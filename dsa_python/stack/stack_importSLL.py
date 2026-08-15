# Import module containing Singly Linked List

from linked_list.singly_linked_list import *

class Stack:
    def __init__(self):
        self.mylist = SLL()         #Creating an object of singly linked list
        self.item_count = 0
        
    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self, data):
        self.mylist.insert_at_first(data)
        self.item_count += 1
        
    def pop(self):
        if not self.is_empty():
            item = self.mylist.start.data
            self.mylist.delete_first()
            self.item_count -= 1
            return item
        else:
            raise IndexError("Stack is empty")    
        
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.data
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return self.item_count
    
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Total elements:",s1.size())
print("Top element:",s1.peek())
print("Deleted element is:", s1.pop())
print("Total elements:",s1.size())
print("Top element:",s1.peek())
    