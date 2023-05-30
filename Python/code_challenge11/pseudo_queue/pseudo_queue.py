class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class Stack:
    def __init__(self):
        self.top=None
    
    def push(self,value):
       
        node=Node(value)
        if self.top==None:
            self.top=node
        else:
            node.next=self.top
            self.top=node

    def pop(self):
        
        try:
            temp=self.top
            self.top=temp.next
            temp.next=None
            return temp.value
        except:
            print("Stack is empty!")

    
            
    def peek(self):
       
       try:
           return self.top.value
       
       except:
            print("Stack is empty!")

    def is_empty(self):
        
        if self.top is None:
            return True
        else:
            return False


class PseudoQueue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,value):
        """
        Inserts a value into the PseudoQueue using a first-in, first-out approach.

        Args:
            value: The value to be inserted.
        """
        self.stack1.push(value)
    
    def dequeue(self):
        """
        Removes and returns the value from the PseudoQueue using a first-in, first-out approach.

        Returns:
            The value at the front of the PseudoQueue.
        """
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise IndexError("PseudoQueue is empty")
        
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
            pop_value=self.stack2.pop()

        
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

        return pop_value
    




if __name__ == "__main__":
    queue = PseudoQueue()
    # queue.enqueue(5)
    # print(queue.stack1.peek())
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    print(queue.stack1.peek())

    output = queue.dequeue()
    print(output)