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
    
 

if __name__ == "__main__":
    node1=Node("node1")
    print(node1)
    node2=LinkedList("node2")
    node2.insert("node1")
    print(node2.insert("node3"))
    print(node2.includes("node1"))
   
