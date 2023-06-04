class Node:
    def __init__(self,value,next=None) :
        self.value=value
        self.next=next

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
class Animal:
    """
    Represents an animal with a species and name.

    Args:
        species (str): The species of the animal.
        name (str): The name of the animal.
    """
    def __init__(self, species, name):
        self.species = species
        self.name = name

class AnimalShelter:
    """
    Represents an animal shelter that can enqueue and dequeue animals.

    Attributes:
        cat_queue (Queue): The queue to store cat animals.
        dog_queue (Queue): The queue to store dog animals.
    """
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, animal):
        """
        Enqueues an animal into the appropriate queue.

        Args:
            animal (Animal): The animal object to enqueue.
        """

        if animal.species == "cat":
            self.cat_queue.enqueue(animal)
        elif animal.species == "dog":
            self.dog_queue.enqueue(animal)

    def dequeue(self, pref):
        """
        Dequeues and returns an animal from the preferred species queue.

        Args:
            pref (str): The preferred species of the animal ("cat" or "dog").

        Returns:
            The dequeued animal from the preferred species queue.
        """
        
        if pref == "cat":
            return self.cat_queue.dequeue()
        elif pref == "dog":
            return self.dog_queue.dequeue()
        else:
            return None


class EmptyError(Exception):
    """
    Custom exception class for empty data structures.
    """
    pass

if __name__ == "__main__":
    shelter = AnimalShelter()
    cat1=Animal("cat","LoLo")
    shelter.enqueue(cat1)
    dog1=Animal("dog","zorro")
    shelter.enqueue(dog1)
    cat2=Animal("cat","lossy")
    shelter.enqueue(cat2)
    dog2=Animal("dog","bogy")
    shelter.enqueue(dog2)
    print("///////////////////////////")
    pref = "cat"
    dequeued_animal = shelter.dequeue(pref)
    print(dequeued_animal.name)
    pref = "dog"
    dequeued_animal = shelter.dequeue(pref)
    print(dequeued_animal.name)
  
   


        