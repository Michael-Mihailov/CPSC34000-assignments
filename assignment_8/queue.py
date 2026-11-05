from record import Record


class Queue:
    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.front = 0
        self.back = 0
        self.table = [None] * size

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def enqueue(self, data: Record):
        if self.isFull():
            return
        self.table[self.front] = data
        self.front = (self.front + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.table[self.back]
        self.back = (self.back + 1) % self.size
        self.count -= 1
        return data