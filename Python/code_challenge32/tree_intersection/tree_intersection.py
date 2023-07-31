from functools import reduce
from operator import add
class Node:
  '''
  A class represent a node in a linked list or other data structure each node has
  two main componenet the value of the node and the reference to the next node.
  args: value
  return : nothing
  '''
  def __init__(self, value):
      self.next=None 
      self.value=value



class LinkedList:
    '''
     A class representing a singly linked list data structure
    '''
    def __init__(self):
        self.head = None


    def insert (self, value):
        '''
        insert a new node with the given value at the begining of the linked list.
        args: value
        output : none
        
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


class HashTable:
    '''
    data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
    
    '''
    def __init__(self,size=1024):
        self.__size=size
        self.__buckets=[None] *size
        self.__keys = []
        
    
    def __hash(self,key):
        '''
        A method to return the hash code of the given key
        arg : key
        output: hash code of the key(index)
        '''
        return reduce(add, [ord(str(char)) for char in str(key)]) * 283 % self.__size

    
        
    def set(self,key,value):
        '''
        Set a key-value pair in the bucket, handling collisions as needed.
        Arguments:
        key : The key to be hashed and used as the identifier for the value.
        value : the value that is aassociated with the key
        Returns: None
        '''
        index = self.__hash(key)
        if self.__buckets[index] is None:
            ll = LinkedList()
            self.__buckets[index] = ll
        
        self.__buckets[index].insert([key,value])
        self.__keys.append(key)
        
        
        

    

    def get(self,key):
        '''
        Retrieve the value with the given key from the hashtable
        arg : key
        return : value or None 
        '''
        index=self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is not None : 
            curr = bucket.head
            while curr :
                if curr.value[0] == key :
                    return curr.value[1]
                curr = curr.next  
        return None  
        
        

    def has(self, key):
        '''
        A method to check if the given key exist in the hashtable.
        arg: key
        output: boolean
        '''
   
        if self.get(key):
            return True
        return False  

        

    def keys(self):
        '''
        args : none
        Returns a list of all the  keys present in the Hashtable.
        '''
        return self.__keys
    
class TreeNode:
    """
        Represents a node in a binary tree.

        Args:
            value: The value stored in the node.
        """
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
        Represents a binary tree.

        The tree is initially empty, with no root node.
        """
    def __init__(self):
        self.root = None

    def in_order(self):
        """
        Performs an in-order traversal on the binary tree and returns a list of node values.

        Returns:
            A list of node values in in-order traversal.
        """
        output = []
        

        def _helper_in_order(root):
            
            if root.left:
                _helper_in_order(root.left)

            
            output.append(root.value)

            if root.right:
                _helper_in_order(root.right)
            
        _helper_in_order(self.root)
        return output

    
def tree_intersection(BT1, BT2):
    '''
    A function that finds the intersection between two binary trees.
    Arguments: two binary trees.
    Return: set of values found in both trees.
    '''

    bt1_values = BT1.in_order()
    bt2_values = BT2.in_order()
    ht1 = HashTable()
    intersection = []
    for value in bt1_values:
        ht1.set(value, value) 
    for value in bt2_values:
        if ht1.has(value):
            intersection.append(value)
       
    return intersection



if __name__ == "__main__":
    # Create BinaryTree 1
    BT1 = BinaryTree()
    BT1.root = TreeNode(150)
    BT1.root.left = TreeNode(100)
    BT1.root.right = TreeNode(250)
    BT1.root.left.left = TreeNode(75)
    BT1.root.left.right = TreeNode(160)
    BT1.root.left.right.left = TreeNode(125)
    BT1.root.left.right.right = TreeNode(175)
    BT1.root.right.left = TreeNode(200)
    BT1.root.right.right = TreeNode(350)
    BT1.root.right.right.left = TreeNode(300)
    BT1.root.right.right.right = TreeNode(500)

    # Create BinaryTree 2
    BT2 = BinaryTree()
    BT2.root = TreeNode(42)
    BT2.root.left = TreeNode(100)
    BT2.root.right = TreeNode(600)
    BT2.root.left.left = TreeNode(15)
    BT2.root.left.right = TreeNode(160)
    BT2.root.left.right.left = TreeNode(125)
    BT2.root.left.right.right = TreeNode(175)
    BT2.root.right.left = TreeNode(200)
    BT2.root.right.right = TreeNode(350)
    BT2.root.right.right.left = TreeNode(4)
    BT2.root.right.right.right = TreeNode(500)
    intersection_set = tree_intersection(BT1, BT2)
    print("Common elements found in both trees:", intersection_set)
