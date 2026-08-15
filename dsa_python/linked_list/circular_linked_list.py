class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
        
class CLL:
    def __init__(self,last = None):
        self.last = last
    
    def is_empty(self):
        return self.last == None
    
    def insert_at_first(self,data):
        n = Node(data)                          # creating a new node with the given data but without any next pointer
        if not self.is_empty():                 # if the CLL is not empty then...
            n.next = self.last.next             # the next pointer of new node(n) will point to the node which was pointing by 'self.last.next' previously
            self.last.next = n                  # now 'self.last.next' will point to the new node(n)....... so a new node is inserted at the beginning
        else:                                   # if the CLL is empty then...
            n.next = n                          # the next pointer of new node(n) will point to itself, so it will be the only node in the CLL
            self.last = n                       # now 'self.last' will point to the new node(n)....... so it will be the only node in the CLL
            
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():                      # if the CLL is empty then...
            n.next = n                           # the next pointer of new node(n) will point to itself, so it will be the only node in the CLL
            self.last = n                        # now 'self.last' will point to the new node(n)....... so it will be the only node in the CLL
        else:
            n.next = self.last.next              # the next pointer of new node(n) will point to the node which was pointing by 'self.last.next' previously
            self.last.next = n                   # now 'self.last.next' will point to the new node(n)....... so a new node is inserted at the end
            self.last = n                        # now 'self.last' will point to the new node(n)....... so it will be the last node in the CLL
                    
    def search(self,data):
        if not self.is_empty():
            temp = self.last.next               # starting from the first node
            while temp != self.last:            # traversing through each node until we reach the last node but not including the last node so we have to check for the last node separately
                if temp.data == data:           # if the data of the current node is equal to the data which we want to search then...
                    return temp                 # we return the current node    
                temp = temp.next                
            if self.last.data == data:          # if the data of the last node is equal to the data which we want to search then...
                return self.last                # we return the last node
        return None     
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next                  # the next pointer of new node(n) will point to the node which was pointing by 'temp.next' previously
            temp.next = n                       # now 'temp.next' will point to the new node(n)....... so a new node is inserted after the given node(temp)
            if temp == self.last:               # if the given node(temp) is the last node then...
                self.last = n                   # now 'self.last' will point to the new node(n)....... so it will be the last node in the CLL
    
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:            # traversing through each node until we reach the last node but not including the last node so we have to check for the last node separately
                print(temp.data,end = " ")      # printing the data of the current node
                temp = temp.next
            print(self.last.data)               # printing the data of the last node
            
    def delete_first(self):
        if self.is_empty():
            pass
        elif self.last.next == self.last:       # if there is only one node in the CLL
            self.last = None                    # so now the CLL will be empty
        else:                                   # if there are more than one nodes in the CLL
            temp = self.last.next               # indicating the first node
            self.last.next = temp.next          # now 'self.last.next' will point to the second node so the first node will be deleted
            temp.next = None                    # removing the next pointer of the deleted node to help garbage collection
             
    def delete_last(self):
        if self.is_empty():
            pass
        elif self.last.next == self.last:
            self.last = None
        else:
            temp = self.last.next               # indicating the first node
            while temp.next != self.last:       # traversing through each node until we reach the second last node
                temp = temp.next                
            temp.next = self.last.next          # now 'temp.next' will point to the first node so the last node will be deleted
            self.last = temp                    # now 'self.last' will point to the second last node so it will be the last node in the CLL
    
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next == self.last:         # if there is only one node in the CLL
                if self.last.data == data:          # if the data of the only node is equal to the data which we want to delete then...
                    self.last = None                # delete the only node in the CLL
            else:                                   # if there are more than one nodes in the CLL    
                if self.last.next.data == data:     # if the data of the first node is equal to the data which we want to delete then...
                    self.delete_first()             # call the delete_first() method to delete the first node
                else:                               # if the data of the first node is not equal to the data which we want to delete then...
                    temp = self.last.next
                    while temp != self.last:        # traversing the CLL
                        if temp.next == self.last:  # if we have to delete the last node then we have to update the last pointer also so we are just calling the delete_last() method
                            if self.last.data == data:
                                self.delete_last()      
                            break
                        if temp.next.data == data:      # if the data of the next node is equal to the data which we want to delete then...
                            temp.next = temp.next.next  # so the next pointer of the current node will point to the node which was pointing by 'temp.next.next' previously
                            break
                        temp = temp.next
    
    def __iter__(self):
        if self.last == None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
                
                        
class CLLIterator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count == 1:          # if we have reached back to the start node
            raise StopIteration                                     # then we stop the iteration
        else:
            self.count = 1
        data = self.current.data
        self.current = self.current.next
        
        return data              
                
    
    
    
cll = CLL()
cll.insert_at_first(20)
cll.insert_at_first(10)
cll.insert_after(cll.search(20),30)
cll.insert_at_last(40)
cll.insert_at_last(50)
for x in cll:
    print(x, end=' ')
cll.delete_first()
print()
cll.print_list()

            
            
            
            