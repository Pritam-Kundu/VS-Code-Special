# We are going to implement Deque using DLL Concept

class Node:
    def __init__(self,prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
        

class Deque:
    def __init__(self):
        self.front = None
        self.rear =  None
        self.item_count = 0
        
    def is_empty(self):
        return self.front == None               
    
    def insert_front(self,data):
        n = Node(None,data,self.front)
        if self.is_empty():                             
            self.front = n                              #If the queue is empty then front and rear both will point to the n
            self.rear = n
        else:                                           #if the queue has some elements beforehand 
            self.front.prev = n                         #because we are using DLL so the prev pointer of front till now must point to n
            self.front = n                              #then front will point to n 
        self.item_count += 1
            
    def insert_rear(self,data):
        n = Node(self.rear,data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:                                           #if the queue is not empty
            self.rear.next = n                          #the next pointer of rear till now will point to n
            self.rear = n                               #then rear will point to n itself
        self.item_count += 1
        
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.front == self.rear:                   #checking whether the deque has only one element or not
            self.front = None                           
            self.rear = None
        else:                                           #if the deque has more than one element in that case
            self.front = self.front.next                #front will be front.next
            self.front.prev = None                      #the prev value of the new front must be None 
        self.item_count -= 1
    
    def delete_rear(self):
        if self.is_empty(): 
            raise IndexError("Deque is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev                  #rear will point to the previous node of rear
            self.rear.next = None                       #the next of new rear will be None
        self.item_count -= 1
        
    def get_front(self):
        if not self.is_empty():
            return self.front.data
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        
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
        