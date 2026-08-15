# Extending list class

class Queue(list):
    def __init__(self):
        self.item_count = 0
        
    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self,data):
        self.append(data)
        self.item_count += 1
        
    def dequeue(self):
        if not self.is_empty():
            self.pop(0)
            self.item_count -= 1
        else:
            raise IndexError("Queue is empty")

    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return len(self)
    
    
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Size is: ",q1.size(),"Front element: ",q1.get_front(),"Rear element: ",q1.get_rear())
q1.dequeue()
q1.enqueue(40)
print("Size is: ",q1.size(),"Front element: ",q1.get_front(),"Rear element: ",q1.get_rear())           