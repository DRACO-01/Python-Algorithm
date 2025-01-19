class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.head.val
        self.head = self.head.next
        if self.head is None:
            # The queue is now empty
            self.tail = None
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.val

    def __len__(self):
        return self.size


# Example usage:
if __name__ == "__main__":
    ll_queue = LinkedListQueue()
    ll_queue.enqueue(1)
    ll_queue.enqueue(2)
    ll_queue.enqueue(3)
    print("Front element:", ll_queue.peek())
    print("Dequeue:", ll_queue.dequeue())
    print("Dequeue:", ll_queue.dequeue())
    ll_queue.enqueue(4)
    ll_queue.enqueue(5)
    while not ll_queue.is_empty():
        print("Dequeue:", ll_queue.dequeue())

