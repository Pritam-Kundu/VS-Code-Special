class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
        
class BST:
    def __init__(self):
        self.root = None
        
    def is_empty(self):
        return self.root==None
        
    def insert(self,item):                         # Insert an item in the BST
        self.root = self.rinsert(self.root,item)   # Call the recursive insert function
        
    def rinsert(self, root, item):                  # Recursive insert function
        if root is None:                            # If the root is None, create a new node with the item and return it
            return Node(item)
        if item < root.item:                                # If the item is less than the root's item, insert it in the left subtree
            root.left = self.rinsert(root.left, item)       # Call the recursive insert function on the left subtree and update the left child of the root
        elif item > root.item:                              # If the item is greater than the root's item, insert it in the right subtree
            root.right = self.rinsert(root.right, item)      # Call the recursive insert function on the right subtree and update the right child of the root
        return root                                 # Return the root of the subtree after inserting the item
    
    def search(self, item):                         # Search for an item in the BST
        return self.rsearch(self.root, item)        # Call the recursive search function
    
    def rsearch(self, root, item):
        if root is None or root.item == item:       # If the root is None or the root's item is equal to the item, return the root(means the node is returned if the item is found, otherwise None is returned)
            return root
        if item < root.item:                        # If the item is less than the root's item, search for it in the left subtree
            return self.rsearch(root.left, item)    # Call the recursive search function on the left subtree and return the result
        else:                                       # If the item is greater than the root's item, search for it in the right subtree
            return self.rsearch(root.right, item)   # Call the recursive search function on the right subtree and return the result
     
    def inorder(self):                              # Doing an inorder traversal of the BST and returning the result as a list
        result=[]
        self.rinorder(self.root, result)
        return result
    
    def rinorder(self, root, result):               # Recursive function for inorder traversal of the BST, it takes the root of the subtree and the result list as input and appends the items in the result list in inorder traversal order
        if root is not None:
            self.rinorder(root.left, result)        # Call the recursive function on the left subtree
            result.append(root.item)                # Append the root's item to the result list
            self.rinorder(root.right, result)       # Call the recursive function on the right subtree
         
    def preorder(self):                             # Doing a preorder traversal of the BST and returning the result as a list
        result=[]
        self.rpreorder(self.root, result)
        return result 
    
    def rpreorder(self, root, result):              # Recursive function for preorder traversal of the BST, it takes the root of the subtree and the result list as input and appends the items in the result list in preorder traversal order
        if root is not None:
            result.append(root.item)                # Append the root's item to the result list
            self.rpreorder(root.left, result)       # Call the recursive function on the left subtree
            self.rpreorder(root.right, result)      # Call the recursive function on the right subtree
            
    def postorder(self):                            # Doing a postorder traversal of the BST and returning the result as a list   
        result = []
        self.rpostorder(self.root, result)
        return result
    
    def rpostorder(self, root, result):             # Recursive function for postorder traversal of the BST, it takes the root of the subtree and the result list as input and appends the items in the result list in postorder traversal order
        if root is not None:
            self.rpostorder(root.left, result)      # Call the recursive function on the left subtree
            self.rpostorder(root.right, result)     # Call the recursive function on the right subtree
            result.append(root.item)                # Append the root's item to the result list