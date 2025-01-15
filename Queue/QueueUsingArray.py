class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None  # Not strictly necessary
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def __str__(self):
        return str(self.queue)


# Example usage:
if __name__ == "__main__":
    q = ArrayQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue after enqueues:", q)
    print("Dequeue:", q.dequeue())
    print("Peek:", q.peek())
    print("Queue now:", q)
