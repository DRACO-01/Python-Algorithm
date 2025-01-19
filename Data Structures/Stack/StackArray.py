class StackArray:
    def __init__(self):
        self.stack = []  # Initialize an empty list to store stack elements

    def push(self, value):
        """Add an element to the top of the stack."""
        self.stack.append(value)
        print(f"Pushed {value} to the stack")

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        """View the top element without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display the stack."""
        print("Stack:", self.stack)


# Usage
stack_array = StackArray()
stack_array.push(10)
stack_array.push(20)
stack_array.push(30)
print("Top element:", stack_array.peek())
print("Popped element:", stack_array.pop())
stack_array.display()
