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
                    self.left = Node(value)

                else:
                    self.left.add_node(value)

            elif self.value < value:
                if self.right == None:
                    self.right = Node(value)
                
                else:
                    self.right.add_node(value)

            else:
                self.count +=1

    def get_min(self):

        while self.left != None:
            print(self.value)
            self = self.left
            
        return self.value

btree = BTree(10)
btree.add_node(5)
btree.add_node(100)
btree.add_node(1)
btree.add_node(14)
btree.add_node(12)
btree.add_node(3)

btree.add_node(6)
btree.add_node(9)
btree.add_node(3)
btree.add_node(-1)

print(btree.get_min())