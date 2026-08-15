# We are going to implement Queue by using Singly linked list concept

class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
        
    def is_empty(self):
        return self.item_count == 0
    
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n             #If the list is empty then the front and rear both will point to n[new node] 
            self.rear = n
        else:                          #If the list is not empty
            self.rear.next = n          #the next element of rear will be n
            self.rear = n               #rear will now point to n
        self.item_count += 1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.front == self.rear:         #When its coming here it means that front and rear both can't be None because its already passed the if condition...so this means the queue has only one element
            self.front = None                #If there is only one element and we have to delete that then we have to change both the front and rear
            self.rear = None
            self.item_count -= 1
        else:                               #This is the case where the list contains more than one element
            self.front = self.front.next        #Here we have to just change the front and its done
            self.item_count -= 1
            
    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise IndexError("Queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return self.item_count
    
    
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Size is: ",q1.size(),"Front element: ",q1.get_front(),"Rear element: ",q1.get_rear())
# q1.dequeue()
q1.enqueue(40)
print("Size is: ",q1.size(),"Front element: ",q1.get_front(),"Rear element: ",q1.get_rear())
            
            