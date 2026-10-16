class DSAQueue:

    def __init__(self, size=100):
        self.queue = [None] * size
        self.count = 0

    def enqueue(self, item):
        raise NotImplementedError("Subclass must implement enqueue()")

    def dequeue(self):
        raise NotImplementedError("Subclass must implement dequeue()")

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.queue)

    def getCount(self):
        return self.count

    def __str__(self):
        raise NotImplementedError("Subclass must implement __str__()")


class DSAShufflingQueue(DSAQueue):

    def __init__(self, size=100):
        super().__init__(size)

    def enqueue(self, item):
        if self.isFull():
            raise Exception("Queue is full")
        self.queue[self.count] = item
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item = self.queue[0]
        for i in range(1, self.count):
            self.queue[i - 1] = self.queue[i]
        self.queue[self.count - 1] = None
        self.count -= 1
        return item

    def __str__(self):
        return str([self.queue[i] for i in range(self.count)])


class DSACircularQueue(DSAQueue):

    def __init__(self, size=100):
        super().__init__(size)
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        if self.isFull():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.count -= 1
        return item

    def __str__(self):
        items = []
        idx = self.front
        for _ in range(self.count):
            items.append(self.queue[idx])
            idx = (idx + 1) % len(self.queue)
        return str(items)