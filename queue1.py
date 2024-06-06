from dugum import Dugum as Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, key, value):
        new_node = Node(key, value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp

    def is_empty(self):
        return self.front is None
