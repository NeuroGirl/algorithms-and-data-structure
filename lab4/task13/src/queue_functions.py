class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, max_size):
        self.first = None
        self.last = None
        self.size = 0
        self.max_size = max_size

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def enqueue(self, value):
        if self.isFull():
            return 'Очередь переполнена'
        new_node = Node(value)
        if self.last is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return 'Очередь пуста'
        dequeued_value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.size -= 1
        return dequeued_value

    def peek(self):
        if self.isEmpty():
            return None
        return self.first.value

    def queue_size(self):
        return self.size

if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue.queue_size())
    print(queue.peek())
    queue.dequeue()
    print(queue.queue_size())
    print(queue.peek())