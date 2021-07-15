# Simple Queue Data Structure in python

class Node:

    def __init__(self, value = 0):
        self.value = value
        self.next = None
        self.previous = None

class Queue:

    def __init__(self, length=10,):
        self.length = length
        self.current_length = 0
        self.head = None
        self.tail = None

    
    def enqueue(self, value=0):
        node = Node(value)
        
        if self.head == None:
        
            self.head = self.tail = node
        
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        
        self.current_length +=1

    
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




