# Code Challenge: Class 05: Linked List Implementation & Class 06

![img5](../code_challenge05/image/nodes.png)
![img5_1](../code_challenge05/image/append.png)
![img5_2](../code_challenge05/image/insert_before.png)
![img5_3](../code_challenge05/image/insert_after.png)



# Approach & Efficiency
**insert method:** This method has a time complexity of O(1) since it simply creates a new node and updates the head attribute of the linked list. The space complexity is also O(1) since only one new node is created.

**includes method:** This method has a time complexity of O(n) in the worst case, where n is the number of nodes in the linked list. This is because we need to traverse the entire linked list to check whether a given value exists in it. The space complexity is O(1) since we only use a few variables to keep track of the current node and the result.

**ToString method:** This method has a time complexity of O(n) in the worst case, since we need to traverse the entire linked list to construct the string representation. The space complexity is O(n) since we create a new string object that contains all the values in the linked list.

**append method** is O(n), where n is the number of nodes in the linked list. This is because the method has to traverse the entire linked list to find the last node, so the time it takes to execute grows linearly with the size of the input. The space complexity is also O(1) since only one new node is created.

**insert_before and Insert_After** methods is O(n), where n is the number of nodes in the linked list. This is because in the worst case, the methods have to traverse the entire linked list to find the node with the specified value, so the time it takes to execute grows linearly with the size of the input. The space complexity is also O(1) since only one new node is created.



# Solution
python Python/code_challenge05/New_Implementation/New_Implementation.py

```python
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
```

