class Node:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.next = nextNode

class LinkedList:
    def __init__(self,head=None):
        self.head=head
    
    def insert(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
    
    def includes(self,value):
        current=self.head
        while current:
            if value == current.value:
                return True
            current=current.next
        return False
    
    def ToString(self):
        current=self.head
        new_string=""
        while current:
            new_string+=f"{current.value} -> "
            current=current.next
        new_string+="None"
        return new_string









if __name__ == "__main__":
    node1=Node("node1")
    print(node1.value)
    node2=Node("node2",node1)
    print(node2.value)
    LinkedList1=LinkedList(node2)
    print(LinkedList1.head.value)
    LinkedList1.insert("node")
    LinkedList1.ToString()
    LinkedList1.includes("node3")

    
