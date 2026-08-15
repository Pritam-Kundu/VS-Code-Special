from linked_list.doubly_linked_list import *

class Deque(DLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
        
    def is_empty(self):
        return super().is_empty()
    
    def insert_front(self, data):
        self.insert_at_first(data)
        self.item_count += 1
        
    def insert_rear(self, data):
        self.insert_at_last(data)
        self.item_count += 1
        
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.delete_first()
            self.item_count -= 1
            
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.delete_last()
            self.item_count -= 1
            
    def get_front(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("Deque is empty")
        
    def get_rear(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != None:
                temp =temp.next
            return temp.data
        else:
            raise IndexError("Deque is empty")
        
    def size(self):
        return self.item_count
    
    

q1 = Deque()
q1.insert_front(20)
q1.insert_front(10)
q1.insert_rear(30)
q1.insert_rear(40)
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())
q1.delete_front()
q1.delete_rear()
q1.delete_rear()
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())
    