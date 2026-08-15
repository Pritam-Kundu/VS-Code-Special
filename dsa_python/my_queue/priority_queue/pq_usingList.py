#Priority can be marks based where the more priority number means more priority 
#Or can be rank based where less priority number means more priority
#We are gonna use this rank based priority system here

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
       
    def push(self,data,priority):                           #Taking input data and priority of that data
        index = 0                                           #At first the index is initialized with 0 as we gonna use it in loop
        while index<len(self.items) and self.items[index][1]<=priority:         #At first we are checking whether the index is less than the length of the list if yes then it going to check the second condition which states that go to the index specified in the list then check the priority of that index if it's less than or equal to the prority specified then continue the loop
            index += 1                                      #Go to the next index and check the condition again
        self.items.insert(index,(data,priority))            #If any of the condition becomes false and we come out of the loop then insert a tuple containing (data, priority) at the specified index
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.items.pop(0)[0]                         #pop() method by default returns the last element but we want that the element with highest priority will be removed first which resides in the first index so we have passed 0 in the pop() method and it will return the tuple but we want only data so we have specified [0] after it
    
    def size(self):
        return len(self.items) 
    
    
p = PriorityQueue()
p.push("Pritam",8)
p.push("Priti",2)
p.push("Saswati",3)
p.push("Shreya",9)
p.push("Prem",7)
p.push("Madhu",5)
p.push("Sanjay",1)

while not p.is_empty():
    print(p.pop())