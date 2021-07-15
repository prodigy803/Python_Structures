class Node:
    # Here the Node class is the structure that holds the values and the intrinsic structure of the DS.
    def __init__(self, value = 0,):
        self.value = value
        self.next = None
        self.previous = None

class Stack:
    # The init class will contain the head and the tail.
    def __init__(self,length = 10):
        self.head = None
        self.tail = None
        self.length = length
        self.current_length = 0

    # append adds an "node" to the end of the "Stack", which we will later modify to add other nodes
    def append(self,value=0):
        
        node = Node(value)

        if self.head == None:

            self.head = self.tail = node
            self.current_length +=1
        
        elif self.current_length < self.length:

            previous_tail = self.tail

            self.tail = node

            self.tail.previous = previous_tail
            
            self.tail.previous.next = self.tail

            self.current_length +=1


    def pop(self):
        
        # Return and remove the top or the tail of the stack:

        if self.current_length == 0:
            return "Stack is empty"
        
        else:

            value_to_be_returned = self.tail.value

            self.tail = self.tail.previous

            self.current_length -=1

            return value_to_be_returned

    def peek(self):

        # Returns the tail or the top of the stack:

        if self.current_length ==0:
            return 'Stack is Empty'
        else:

            return self.tail.value


stack1 = Stack()

stack1.append(10)
stack1.append(123)
stack1.append(330)
stack1.append(10)
stack1.append(550)
stack1.append(166)
stack1.append(1000)

print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())

