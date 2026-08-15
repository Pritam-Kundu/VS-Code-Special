class Deque(list):
    def __init__(self):
        pass
    
    def is_empty(self):
        return len(self) == 0
    
    def insert_front(self, data):
        self.insert(0, data)
        
    def insert_rear(self, data):
        self.append(data)
        
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.pop(0)
        
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.pop()
            
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Deque is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Deque is empty")
        
    def size(self):
        return len(self)
    
    
q1 = Deque()
q1.insert_front(20)
q1.insert_front(10)
q1.insert_rear(30)
q1.insert_rear(40)
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())
q1.delete_front()
q1.delete_rear()
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())