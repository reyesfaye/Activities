class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print (items)


q = Queue()
print(q.isEmpty())
q.enqueue("n")
q.enqueue("e")
q.enqueue("y")
q.enqueue("a")
q.enqueue("f")
q.enqueue(9)
q.printqueue()
q.dequeue()
print("\n")
q.printqueue()
