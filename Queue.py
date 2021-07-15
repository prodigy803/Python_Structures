# Simple Queue Data Structure in python

class Node:
    # Here we create a simple Node class, which will act as the container structure for the "Queue"

    def __init__(self, value = 0):
        self.value = value
        
        # Both the Next and the Previous will be helpful in keeping track of the state of the "Queue"
        self.next = None
        self.previous = None

class Queue:

    # Here we will track the following:
    # The length
    # The head and the tail
    # The head and tail will help us achieve a time complexity of O(1)
    def __init__(self, length=10,):
        self.length = length
        self.current_length = 0
        self.head = None
        self.tail = None

    # Here we are tracking the "Enqueing" process
    # If its the first node, set the head and tail as the first node
    # Else:
    #  set the tail.next as the new node   
    #  reset the new nodes previous as the old node (tail)
    #  set the tail as the new node

    def enqueue(self, value=0):
        node = Node(value)
        
        if self.head == None:
        
            self.head = self.tail = node
        
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        
        self.current_length +=1

    # Here we are tracking the dequeing function:
    # Very simple, 
    # Fetch the head value, set the next node as head (self.head)
    # if the queue is empty, print "Queue is empty"
    
    def dequeue(self):
        
        if self.head !=None:

            to_be_returned = self.head.value

            self.head = self.head.next

            self.current_length -=1

            if self.current_length == 0:
                self.head = self.tail = None

            return to_be_returned
        
        else:
            
            return "Queue is empty"

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(40)
queue.enqueue(50)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

print(queue.dequeue())
print(queue.dequeue())




