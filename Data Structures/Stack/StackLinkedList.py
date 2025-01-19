class Node:
    """A node in the linked list."""
    def __init__(self, value):
        self.value = value  # Store the value
        self.next = None  # Pointer to the next node


class StackLinkedList:
    def __init__(self):
        self.top = None  # The top of the stack (initially empty)

    def push(self, value):
        """Add an element to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top to the new node
        print(f"Pushed {value} to the stack")

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.is_empty():
            popped_value = self.top.value
            self.top = self.top.next  # Update the top to the next node
            return popped_value
        else:
            return "Stack is empty!"

    def peek(self):
        """View the top element without removing it."""
        if not self.is_empty():
            return self.top.value
        else:
            return "Stack is empty!"

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def display(self):
        """Display the stack."""
        current = self.top
        stack_values = []
        while current:  # Traverse the linked list
            stack_values.append(current.value)
            current = current.next
        print("Stack:", stack_values)


# Usage
stack_linked_list = StackLinkedList()
stack_linked_list.push(10)
stack_linked_list.push(20)
stack_linked_list.push(30)
print("Top element:", stack_linked_list.peek())
print("Popped element:", stack_linked_list.pop())
stack_linked_list.display()
