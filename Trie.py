
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

    def getNode():
        return Node()

    def insert(self, value):
        
        ## essentially we are going to create a list of lists (like a organized nest of lists)
        temp_node = self.root
        len_of_word = len(value)

        for i in range(len_of_word):
            index = self.get_index_of_letter(value[i])

            if temp_node.nodes[index] == None:
                temp_node.nodes[index] = Node()

            temp_node = temp_node.nodes[index]

        temp_node.isEndOfWord = True


    def search(self, value):
        temp_node = self.root
        len_of_word = len(value)

        for i in range(len_of_word):
            index = self.get_index_of_letter(value[i])

            if temp_node.nodes[index] == None:
                return False
            
            temp_node = temp_node.nodes[index]

        return temp_node.isEndOfWord

trie = Trie()

trie.insert(value = 'glasses')
trie.insert(value = 'glass')
trie.insert(value = 'chashma')

print(trie.search('glas'))


