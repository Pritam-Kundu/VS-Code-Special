class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start
    def is_empty(self):
        return self.start == None       #if start is None then the LL is empty so True is returned
    
    def insert_at_first(self, data):
        n = Node(data, self.start)    # the next pointer of new node(n) will point to the the node which was pointing by 'start' previously
        self.start = n                # now 'start' will point to the new node(n)....... so a new node is inserted at first

    def insert_at_last(self,data):
        n = Node(data)                  #the value of next has been by default set to None so no need to pass the next
        if not self.is_empty():         #checking if the LL is empty or not,if not empty then...
            temp = self.start           #a temporary variable is created which is named as temp and it's also starting from start
            while(temp.next is not None):       #the loop will continue until temp.next is not None, meaning we want the last node in temp
                temp = temp.next        #until we reach the last node, we will traverse through each node one by one
            temp.next = n               #when we reach the end, then new node(n) is appended at last
        else:                           #if the LL is empty then...
            self.start = n              #start will directly point to the new node(n)

    def search(self,data):
        temp = self.start
        while(temp is not None):        #we have not used temp.next because we want to check the last node as well
            if (temp.data == data):
                return temp
            temp = temp.next
        return None                     #if the data is not found in the LL then None is returned
    
    def insert_after(self,temp, data):      # Here 'temp' is the node after which we want to insert the new node and data is the value of new Node, [we can also get the node by using search method by passing the data]
        if temp is not None:
            n = Node(data, temp.next)       #the next pointer of new node(n) will point to the the node which was pointing by 'temp.next' previously
            temp.next = n                   #now 'temp.next' will point to the new node(n)....... so a new node is inserted after the node 'temp'

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data,end=' ')        #printing the data of each node
            temp = temp.next

    def delete_first(self):
        if self.start is not None:          #if the LL is not empty then...
            self.start = self.start.next    #start will point to the next node of the first node, so the first node is deleted
    
    def delete_last(self):                  #there can be 3 cases: 1. LL has no node, 2. LL has only one node, 3. LL has more than one node
        if self.start is None:              #if the LL has no node then...
            pass                            #nothing will happen
        elif self.start.next is None:       #if the LL has only one node then...
            self.start = None               #start will point to None, so the only node is deleted
        else:                               #if the LL has more than one node then...(means at least 2 nodes are there)
            temp = self.start
            while temp.next.next is not None:   #we want to reach the second last node
                temp = temp.next                #traversing through each node
            temp.next = None                    #the next pointer of second last node will point to None, so the last node is deleted

    def delete_item(self, data):                #it will delete the node which has the data value
        if self.start is None:                  #if the LL is empty then...
            pass
        elif self.start.next is None:           #if the LL has only one node then...
            if self.start.data == data:         #and if the data of the only node is equal to the data which we want to delete then...
                self.start = None               #the only node is deleted
        else:                                   #if the LL has more than one node then...
            temp = self.start                   
            if temp.data == data:               #if the data of the first node is equal to the data which we want to delete then...
                self.start = temp.next          #the first node is deleted
            else:
                while temp.next is not None:        #if the data is not in the first node then we will traverse through each node
                    if temp.next.data == data:      #if the next node of temp has the data which we want to delete then we will stop there
                        temp.next = temp.next.next     #the next pointer of temp will point to the next node of the node which we want to delete
                        break                       #and the loop will break, no need to do temp.next
                    temp = temp.next

    def __iter__(self):                             #this method is used to iterate through the nodes of the LL...[Ratta marooo]
        return SLLIterator(self.start)

class SLLIterator:                              #this class is used to iterate through the nodes of the LL...[Ratta marooo]
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


'''
myList = SLL()
myList.insert_at_first(20)
myList.insert_at_first(10)
myList.insert_at_last(30)
myList.insert_after(myList.search(20),25)
myList.print_list()
print()
myList.delete_item(30)

for x in myList:
    print(x, end = ' ')
'''
