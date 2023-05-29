class Node:
    def __init__(self,value,next=None) :
        self.value=value
        self.next=next

class Stack:
    def __init__(self,top=None):
        self.top=top

    def push(self,value):
        node=Node(value)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node

    def pop(self):
        if self.top is None:
            raise EmptyError("Stack is empty!")
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
        return temp.value
    
    def peek(self):
        if self.top is None:
            raise EmptyError("Stack is empty!")
        else:
            return self.top.value
        
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False
        

    def __str__(self):
        current=self.top
        string=""
        while current:
           string+= f"{current.value} -> "
           current=current.next
        return string+"None"

        
class Queue:
    def __init__(self,front=None,back=None):
        self.front=front
        self.back=back
        
    def enqueue(self,value):
        node=Node(value)
        if self.front is None:
            self.back=node
            self.front=node
        else:
            self.back.next=node
            self.back=node
    
    def dequeue(self):
        if self.front is None:
            raise EmptyError("Stack is empty!")
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None
        return temp.value
    
    def peek(self):
        if self.front is None:
            raise EmptyError("Stack is empty!")
        else:
            return self.front.value
        
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
        
    def __str__(self):
        current=self.front
        string=""
        while current:
           string+= f"{current.value} -> "
           current=current.next
        return string+"None"

class EmptyError(Exception):
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