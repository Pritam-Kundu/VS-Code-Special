#Here we are going to use Linked List Concept to implement Priority Queue

class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next
        
    
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
        
    def is_empty(self):
        return self.item_count == 0
        
    def push(self,item,priority):
        n = Node(item,priority)
        if self.start == None or self.start.priority > priority:            #Basically we are inserting at first so there are 2 possibilities when we do this--i) the linked list is empty or ii) the priority of new node is less than the priority of the first node
            n.next = self.start                                             #Inserting the new node at first
            self.start = n
        else:                                                               #Means we have to insert in between or at last
            temp = self.start                                               #So we have to traverse 
            while temp.next != None and temp.next.priority <= priority:     #Loop will continue until--i)temp.next is not none(until the list is not ended) and ii) the priority of new node is bigger than or equal to the priority of temp.next node
                temp = temp.next 
            n.next = temp.next
            temp.next = n
        self.item_count += 1    
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        
    def size(self):
        return self.item_count
    
    
        
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