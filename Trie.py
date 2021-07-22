
from typing import get_args


class Node:

    def __init__(self):
        self.nodes = [None]*26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = Node()

    def get_index_of_letter(self, value):

        return ord(value.lower()) - ord('a')


    def insert(self, value):
        
        ## essentially we are going to create a list of lists (like a organized nest of lists)

        for i in range(len(value)):
            index = self.get_index_of_letter(value[i])

            if self.root.nodes[index] == None:
                self.root.nodes[index] = Node()

            self.root = self.root.nodes[index]

        self.root.isEndOfWord = True

    def search(self, value):

        for i in range(len(value)):
            index = self.get_index_of_letter(value[i])
            temp_node = self.root

            if temp_node.nodes[index] == None:
                return False
            
            temp_node = temp_node.nodes[index]

        return temp_node.isEndOfWord

trie = Trie()

trie.insert('glasses')
trie.insert('glass')
trie.insert('chashma')

# trie.get_root()

print(trie.search('gla'))


