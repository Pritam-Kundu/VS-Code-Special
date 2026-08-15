from linked_list.singly_linked_list import *

class Queue(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
        
    def is_empty(self):
        return super().is_empty()
    
    def enqueue(self, data):
        self.insert_at_last(data)
        self.item_count += 1
        
    def dequeue(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("Queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != None:
                temp = temp.next
            return temp.data
        else:
            raise IndexError("Queue is empty")
    
    def size(self):
        return self.item_count
    
    
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Size is: ",q1.size(),"Front element: ",q1.get_front(),"Rear element: ",q1.get_rear())
q1.dequeue()
q1.enqueue(40)
print("Size is: ",q1.size(),"Front element: ",q1.get_front(),"Rear element: ",q1.get_rear())