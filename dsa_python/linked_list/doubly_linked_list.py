class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL: 
    def __init__(self,start = None):
        self.start = start      
        
    def is_empty(self):
        return self.start == None
    
    def insert_at_first(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():             # if list is not empty
            self.start.prev = n             # update the previous pointer of the current start node 
        self.start = n
            
    def insert_at_last(self, data):
        temp = self.start                   # temp is used to get the last node if there is no node in the list then it will be None
        if self.start != None:              # if list is not empty
            while temp.next is not None:    # traverse to the last node
                temp = temp.next
        
        # Now temp.next is None whether for there is no node or there are nodes in the lists
        n = Node(temp, data, None)
        if temp == None:                    # if the list is empty
            self.start = n
        else:                               # the list has some elements and we have the last node in temp
            temp.next = n
        
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp , data):
        if temp is not None:                    # temp is the node after which we want to insert the new node
            n = Node(temp, data, temp.next)
            if temp.next is not None:           # if temp.next is not None then we need to update the previous pointer of the next node
                temp.next.prev = n
            temp.next = n                       # now 'temp.next' will point to the new node(n)....... so a new node is inserted after the node 'temp'
                
    def insert_before(self, temp, data):
        if temp is not None:
            n = Node(temp.prev, data, temp)     
            if temp.prev is not None:           # if temp.prev is not None then we need to update the next pointer of the previous node
                temp.prev.next = n              # so the previous node will point to the new node(n)
            temp.prev = n                       # now 'temp.prev' will point to the new node(n)....... so a new node is inserted before the node 'temp'
            
    def delete_first(self):
        if self.start is not None:              # if the DLL is not empty then...
            self.start = self.start.next        # start will point to the next node of the first node, so the first node is deleted
            if self.start is not None:          # if the list is not empty after deletion means there was more than one node
                self.start.prev = None          # the previous pointer of the new start node will be None
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next.prev = None
            temp.next = None
    
    def delete_item(self, data):
        if self.start is None:                              # if the list is empty then nothing to delete
            pass
        else:
            temp = self.start
            while temp is not None:                         # traverse the list to find the node with the given data
                if temp.data == data:
                    if temp.next is not None:               # if the node to be deleted is not the last node
                        temp.next.prev = temp.prev          # update the previous pointer of the next node
                    if temp.prev is not None:               # if the node to be deleted is not the first node
                        temp.prev.next = temp.next          # update the next pointer of the previous node
                    else:
                        self.start = temp.next              # if the node to be deleted is the first node then update the start pointer
                    break
                temp = temp.next
           
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
            
    def __iter__(self):
        return DLLIterator(self.start)

class DLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    
# mylist = DLL()
# mylist.insert_at_first(20)
# mylist.insert_at_first(10)
# mylist.insert_at_first(5)
# mylist.insert_at_last(50)
# mylist.insert_at_last(60)
# mylist.insert_after(mylist.search(10),15)
# mylist.insert_before(mylist.search(50),30)
# mylist.print_list()
# print()
# mylist.delete_item(60)
# for x in mylist:
#     print(x, end=" ")

