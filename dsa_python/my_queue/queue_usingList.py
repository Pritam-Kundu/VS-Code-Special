# Define an empty list object as instance object member of Queue


class Queue:
    def __init__(self):
        self.mylist = []
        self.item_count = 0
        
    def is_empty(self):
        return self.mylist == 0
    
    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("Queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            # index = len(self.mylist) - 1
            return self.mylist[-1]
        else:
            raise IndexError("Queue is empty")
        
    def enqueue(self, data):
        self.mylist.append(data)
        self.item_count += 1
        
    def dequeue(self):
        if not self.is_empty():
            del self.mylist[0]
            self.item_count -= 1
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return self.item_count
    
    
    
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())
q1.dequeue()
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())
q1.enqueue(40)
print("Size is:",q1.size()," Front is:",q1.get_front()," Rear is:",q1.get_rear())