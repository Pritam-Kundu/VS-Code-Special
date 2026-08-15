class Node:
    def __init__(self,prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
        
        
class CDLL:
    def __init__(self,start=None):
        self.start = start
        
    def is_empty(self):
        return self.start == None
    
    def insert_at_first(self,data):
        n = Node()
        n.data = data
        if self.is_empty():                 # if the list is empty
            n.next = n                      # n.next points to itself
            n.prev = n                      # n.prev points to itself
            self.start = n                  # self.start points to n
        else:                               # if the list is not empty
            n.next = self.start             # n.next points to start
            n.prev = self.start.prev        # n.prev points to the last node
            self.start.prev.next = n        # last node's next points to n
            self.start.prev = n             # start.prev points to n
            self.start = n                  # self.start points to n
        
    def insert_at_last(self,data):
        n = Node()
        n.data = data
        if self.is_empty():                 # if the list is empty
            n.next = n                      # n.next points to itself
            n.prev = n                      # n.prev points to itself
            self.start = n                  # self.start points to n
        else:                               # if the list is not empty
            n.prev = self.start.prev        # n.prev points to the last node
            n.next = self.start             # n.next points to start
            self.start.prev.next = n        # last node's next points to n
            self.start.prev = n             # start.prev points to n
            
    def search(self,data):
        if not self.is_empty():
            temp = self.start                       # temp points to start
            while temp.next != self.start:          # traverse the list until the last node
                if temp.data == data:               # if data is found
                    return temp                     # return the node  
                temp = temp.next                    # move to the next node
            if self.start.prev.data == data:        # check the last node as it is not checked in the loop
                return self.start.prev              # return the last node if data is found
            return None
        
    def insert_after(self,temp,data):
        if temp is not None: 
            n = Node()
            n.data = data
            n.next = temp.next                      # n.next points to temp's next node
            n.prev = temp                           # n.prev points to temp   
            temp.next.prev = n                      # temp's next node's prev points to n
            temp.next = n                           # temp's next points to n   
            
    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.data,end=' ')
                temp = temp.next
            print(self.start.prev.data)

    def delete_first(self):
        if self.is_empty():
            pass
        elif self.start.next == self.start:         # if there is only one node
            self.start = None                       # make the list empty   
        else:                                       # if there are more than one nodes 
            self.start.prev.next = self.start.next      # last node's next points to second node
            self.start.next.prev = self.start.prev      # second node's prev points to last node
            self.start = self.start.next                # self.start points to second node ... so finally first node is deleted
            
    def delete_last(self):
        if self.is_empty():
            pass
        elif self.start.next == self.start:
            self.start = None
        else:
            self.start.prev.prev.next = self.start          # second last node's next points to start
            self.start.prev = self.start.prev.prev          # start.prev points to second last node ... so finally last node is deleted
            
    def delete_item(self,data):
        if self.is_empty():
            pass
        elif self.start.next == self.start:                 # if there is only one node
            if self.start.data == data:                     # if the data is found in that node 
                self.start = None                           # make the list empty 
        else:                                               # if there are more than one nodes 
            temp = self.start                               # temp points to start    
            if self.start.data == data:                     # if the data is found in the first node 
                self.delete_first()                         # then delete the first node by calling delete_first() method
                return
            while temp.next != self.start:                  # otherwise traverse the list until the last node
                if temp.next.data == data:                  # if the data is found in the next node of temp 
                    if temp.next == self.start.prev:             # Refer to: https://chatgpt.com/share/68b1d137-102c-8009-82b1-aca936076061 
                        self.start.prev = temp              # if the node to be deleted is the last node, update start.prev to point to temp
                    temp.next.next.prev = temp              # temp's next node's next node's prev points to temp
                    temp.next = temp.next.next              # temp's next points to temp's next node's next ... so finally the node is deleted
                    break
                temp = temp.next
    
    def __iter__(self):
        return CDLLIterator(self.start)
                
                
class CDLLIterator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0                      # its like a flag variable 
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:               # in first case self.count is 0 so it will not stop
            raise StopIteration
        else:
            self.count = 1                                              # in next iterations self.count is 1 so it will stop 
        data = self.current.data
        self.current = self.current.next
        return data
                
    

mylist = CDLL()
mylist.insert_at_last(100)
mylist.insert_at_first(20)
mylist.insert_at_first(10)
mylist.insert_after(mylist.search(20),30)
mylist.insert_at_last(150)

for x in mylist:
    print(x,end=' ')

mylist.delete_item(150)
print()
mylist.print_list()


