#Create an empty list object as instance object member of the class Deque

class Deque:
    def __init__(self):
        self.mylist = []
        
    def is_empty(self):
        return len(self.mylist) == 0
    
    def insert_front(self, data):
        self.mylist.insert(0, data)
        
    def insert_rear(self, data):
        self.mylist.append(data)
        
    def delete_front(self):
        if not self.is_empty():
            self.mylist.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def delete_rear(self):
        if not self.is_empty():
            self.mylist.pop()
        else:
            raise IndexError("Queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("Queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return len(self.mylist)
    
    
q1 = Deque()
q1.insert_front(20)
q1.insert_front(10)
q1.insert_rear(30)
q1.insert_rear(40)
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())
q1.delete_front()
q1.delete_rear()
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())

    