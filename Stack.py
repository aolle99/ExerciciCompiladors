class Stack:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.stack = [{}]

    # Get the current size of the stack
    def getSize(self):
        return len(self.stack)

    # Check if the stack is empty
    def isEmpty(self):
        return self.getSize() == 0

    # Get the top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.stack[self.getSize()-1]

    # Push a value into the stack.
    def push(self):
        self.stack.append({})

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        self.stack.pop()