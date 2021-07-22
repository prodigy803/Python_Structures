# I believe my solution maybe verbose, but its intuitive and easily explanable for anyone (with basic knowledge of recursion and pointers)

## The del function has been split up into multiple brackets so its easy for anyone to understand.

class Btree:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

    def add_node(self,value):

        if self.value == None:
            self.value = value

        else:

            if self.value > value:
                if self.left == None:
                    self.left = Btree(value)
                else:
                    self.left.add_node(value)

            elif self.value < value:
                if self.right == None:
                    self.right = Btree(value)
                
                else:
                    self.right.add_node(value)

            else:
                self.count +=1
 

    def inorder_traverse(self):
        if self.left != None:
            self.left.inorder_traverse()

        for i in range(self.count):
            print(self.value)

        if self.right != None:
            self.right.inorder_traverse()

    def delete_node(self, value = 0, root_node = None, left_traverse = None, right_traverse = None):
        
        ## There are three situations where a delete function will take place
        ## 1. Where the node to be deleted have no sub-nodes
        ## 2. Where the node to be deleted have just one child
        ## 3. Where the node to be deleted have 2 children

        if value < self.value:
            self.left.delete_node(root_node = self, value = value, left_traverse=True, right_traverse=False)

        elif value > self.value:
            self.right.delete_node(root_node = self, value = value, left_traverse=False, right_traverse=True)

        if self.value == value and self.count == 1:
            # This is for the first situation
            if (self.left == None) and (self.right== None):
                if left_traverse == True:
                    root_node.left = None
                if right_traverse == True:
                    root_node.right = None

            ## This is for the second situation
            elif ((self.left == None) and (self.right != None)):
                
                if left_traverse == True:
                    root_node.left = self.right
                if right_traverse == True:
                    root_node.right = self.right

            
            elif ((self.left != None) and (self.right == None)):
                if left_traverse == True:
                    root_node.left = self.left
                if right_traverse == True:
                    root_node.right = self.left

            ## now the third situation is a bit more tricky as compared to the first two,
            ## Step one to deleting, you need to get the min element of the right sub-tree and substitute that with hit-node

            elif (self.left != None) and (self.right != None):
                ## get right trees min-value and count
                temp_value, temp_count  = self.right.get_min_value_for_del(root_node = self)
                self.value = temp_value
                self.count = temp_count
                
        elif self.count > 1:
            self.count -=1

    def get_min_value_for_del(self, root_node = None):
        if self.left != None:
            return self.left.get_min_value_for_del(root_node = self)

        elif self.left == None:

            if self.right != None:
                root_node.left = self.right
            else:
                root_node.left = None

            return self.value, self.count
    
    def get_min_value(self):
        if self.left != None:
            return self.left.get_min_value()
        else:
            return self.value


btree = Btree(5)
btree.add_node(8)
btree.add_node(10)
btree.add_node(7)
btree.add_node(3)
btree.add_node(4)
btree.add_node(2)
btree.add_node(9)
btree.add_node(9)
btree.add_node(11)

btree.delete_node(value=8)
# btree.delete_node(value=9)

print('Here is the Inorder traversal')
btree.inorder_traverse()

print("MIN VALUE IN BTREE IS: {}".format(btree.get_min_value()))

"""
Output is :

Here is the Inorder traversal
2
3
4
5
7
9
9
10
11
MIN VALUE IN BTREE IS: 2
"""