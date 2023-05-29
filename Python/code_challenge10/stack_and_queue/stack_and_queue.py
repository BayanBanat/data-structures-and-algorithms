class Node:
    def __init__(self,value,next=None) :
        self.value=value
        self.next=next

class Stack:
    """
        Initializes a new instance of the Stack class.

        Args:
            top (Node, optional): The top node of the stack. Defaults to None.
    """
    def __init__(self,top=None):
        self.top=top

    def push(self,value):
        '''
        Pushes a value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        
        '''
        node=Node(value)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node

    def pop(self):
        """
        Removes and returns the value at the top of the stack.

        Returns:
            The value at the top of the stack(value that is remover).

        Raises:
            EmptyError: If the stack is empty.
        """
        if self.top is None:
            raise EmptyError("Stack is empty!")
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
        return temp.value
    
    def peek(self):
        """
        Returns the value at the top of the stack without removing it.

        Returns:
            The value at the top of the stack.

        Raises:
            EmptyError: If the stack is empty.
        """
        if self.top is None:
            raise EmptyError("Stack is empty!")
        else:
            return self.top.value
        
    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        if self.top is None:
            return True
        else:
            return False
        

    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            A string representation of the stack.
        """
        current=self.top
        string=""
        while current:
           string+= f"{current.value} -> "
           current=current.next
        return string+"None"

        
class Queue:
    """
        Initializes a new instance of the Queue class.

        Args:
            front (Node, optional): The front node of the queue. Defaults to None.
            back (Node, optional): The back node of the queue. Defaults to None.
    """
    def __init__(self,front=None,back=None):
        self.front=front
        self.back=back
        
    def enqueue(self,value):
        """
        Adds a value to the back of the queue.

        Args:
            value: The value to be added to the queue.
        """
        node=Node(value)
        if self.front is None:
            self.back=node
            self.front=node
        else:
            self.back.next=node
            self.back=node
    
    def dequeue(self):
        """
        Removes and returns the value at the front of the queue.

        Returns:
            The value at the front of the queue.

        Raises:
            EmptyError: If the queue is empty.
        """
        if self.front is None:
            raise EmptyError("Stack is empty!")
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None
        return temp.value
    
    def peek(self):
        """
        Returns the value at the front of the queue without removing it.

        Returns:
            The value at the front of the queue.

        Raises:
            EmptyError: If the queue is empty.
        """
        if self.front is None:
            raise EmptyError("Stack is empty!")
        else:
            return self.front.value
        
    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        if self.front is None:
            return True
        else:
            return False
        
    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
            A string representation of the queue.
        """
        current=self.front
        string=""
        while current:
           string+= f"{current.value} -> "
           current=current.next
        return string+"None"

class EmptyError(Exception):
    """
    Custom exception class for empty data structures.
    """
    pass






if __name__ == "__main__":

# ////////////Stack///////////
    stack_1=Stack()
    try:
        stack_1.push("e")
        stack_1.push("d")
        stack_1.push("o")
        stack_1.push("c")
        print(stack_1.pop())
        # stack_1.pop()
        # stack_1.pop()
        # stack_1.pop() # raise EmptyError exception
        print(stack_1)
        print(stack_1.is_empty())
        print(stack_1.peek())
        
    except EmptyError:
        print("Stack is empty!")

 # ////////////Queue///////////
    queue_1=Queue()
    try:
       queue_1.enqueue("b")
       queue_1.enqueue("a")
       queue_1.enqueue("y")
       queue_1.enqueue("a")
       queue_1.enqueue("n")
       print(queue_1)
       print(queue_1.dequeue())
       queue_1.dequeue()
       print("111",queue_1.peek())
       print(queue_1.is_empty())

    except EmptyError:
        print("Stack is empty!")