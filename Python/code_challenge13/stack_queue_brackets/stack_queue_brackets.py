class Stack:
    """A stack data structure implemented using a Python list.

    The stack follows the Last-In-First-Out (LIFO) principle. Elements can be added
    to the top of the stack using the `push` method and removed from the top using
    the `pop` method.

    Attributes:
        stack (list): A list to store the elements of the stack.
    """
    def __init__(self):
        self.stack = []
    
    def push(self,value):
        """Add a new element to the top of the stack.

        Args:
            value: The value to be added to the stack.
        """
        self.stack.append(value)
    
    def pop(self):
        """Remove and return the most recently added element from the stack.

        Returns:
            The most recently added element, or None if the stack is empty.
        """
        if not len(self.stack) == 0:
            return self.stack.pop()
        else:
            return None



def validate_brackets(expression):
    """
    This function takes an expression as input and checks if the brackets in the expression are balanced.
    It uses a stack to keep track of opening brackets encountered in the expression and verifies that each
    closing bracket matches the corresponding opening bracket.

    Args:
        expression (str): The expression to validate.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    stack = Stack()
    bracket_list = ["(", "{", "["]
    for char in expression:
        if char in bracket_list:
            stack.push(char)
        elif char == ")":
            if len(stack.stack) == 0 or stack.stack[-1] != "(":
                return False
            stack.pop()
        elif char == "}":
            if len(stack.stack) == 0 or stack.stack[-1] != "{":
                return False
            stack.pop()
        elif char == "]":
            if len(stack.stack) == 0 or stack.stack[-1] != "[":
                return False
            stack.pop()

    return len(stack.stack) == 0



if __name__ == "__main__":
    print(validate_brackets("{(})"))
    print(validate_brackets("{}{Code}[Fellows](())"))