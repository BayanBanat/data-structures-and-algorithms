class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    def includes(self, value):
        current = self.head
        while current:
            if value == current.value:
                return True
            current = current.next
        return False
    
    def ToString(self):
        current = self.head
        New_string = ""
        while current:
            New_string += f"{current.value} -> "
            current = current.next
        New_string += "None"
        return New_string