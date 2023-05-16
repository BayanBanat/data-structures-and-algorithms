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

    def append(self, new_value):
     new_node = Node(new_value)
     if self.head is None:
        self.head = new_node
     else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node


    def insert_before(self, value, new_value):
     new_node = Node(new_value)
     current = self.head
     if current.value == value:
        new_node.next=current
        self.head=new_node
        return
     while current.next:
        if current.next.value == value:
            new_node.next = current.next
            current.next = new_node
            return
        current = current.next

     return
    
    # head -> {1} -> {3} -> {2} -> X	3, 5	head -> {1} -> {5} -> {3} -> {2} -> X
    
    def Insert_After(self, value, new_value):
     new_node = Node(new_value)
     current = self.head

     while current:
        if current.value == value:
            if current.next is None:
                current.next = new_node
                new_node.next = None
            else:
                new_node.next = current.next
                current.next = new_node
            return
        current = current.next

        
# head -> {1} -> {2} -> {2} -> X	2, 5	head -> {1} -> {2} -> {5} -> {2} -> X




        










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
    node3=LinkedList()
    print(node3.append("node4"))
    print(node3.insert_before("node2","node4"))

    
