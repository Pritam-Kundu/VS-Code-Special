#Define __init__() method to create an empty list object as instance object member of Stack

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == 0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()             # pop also returns the deleted item so we have used return statement
        else: 
            raise IndexError("Stack is empty")       
    def peek(self):
        if not self.is_empty():
            return self.items[-1]               #index -1 will point to the last element in the list
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
            
            
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is:",s1.peek())
print("Removed element is:",s1.pop())
print("Top element is:",s1.peek())