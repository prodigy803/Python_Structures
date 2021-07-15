class Node:
    
    def __init__(self, value = 0,):
        self.value = value
        self.next = None
        self.previous = None

class Stack:

    def __init__(self,length = 10):
        self.head = None
        self.tail = None
        self.length = length
        self.current_length = 0

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

        if self.current_length == 0:
            return "Stack is empty"
        
        else:

            value_to_be_returned = self.tail.value

            self.tail = self.tail.previous

            self.current_length -=1

            return value_to_be_returned

    def peek(self):

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

