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


# head -> {1} -> {3} -> {8} -> {2} -> X	0	2
    def linked_list_kth(self,k):
       current=self.head
       normal_list=[]
       while current:
          normal_list.insert(0, current.value)
          current=current.next
       if k>=len(normal_list) or k<-len(normal_list):
          raise ValueError("Invalid value of k")
       return normal_list[k]
    
    
# {1} -> {3} -> {2} -> null	{5} -> {9} -> {4} -> null	{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> null
# {1} -> {3} -> null	{5} -> {9} -> {4} -> null	{1} -> {5} -> {3} -> {9} -> {4} -> null
def linked_list_zip(LL1=None, LL2=None):
    merged_list = LinkedList()

    pointer1 = LL1.head
    pointer2 = LL2.head

    while pointer1 and pointer2:
        merged_list.append(pointer1.value)
        merged_list.append(pointer2.value)
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    if pointer1 is not None:
        merged_list.append(pointer1.value)

    if pointer2 is not None:
        merged_list.append(pointer2.value)

    if LL1.head is None:
        return LL2

    if LL2.head is None:
        return LL1

    return merged_list

















