class DSAStack:

    def __init__(self, size=100):
        self.stack = [None] * size
        self.count = 0

    def push(self, item):
        if self.count == len(self.stack):
            raise Exception("Stack is full")
        self.stack[self.count] = item
        self.count += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        self.count -= 1
        item = self.stack[self.count]
        self.stack[self.count] = None
        return item

    def top(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[self.count - 1]

    def isEmpty(self):
        return self.count == 0

    def getCount(self):
        return self.count

    def __str__(self):
        return str([self.stack[i] for i in range(self.count)])