class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} enqueued to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data = self.front.data
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None 
        del temp  
        print(f"{data} dequeued from queue")
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def is_full(self):
        
        return False

    def free_queue(self): 
        while not self.is_empty():
            self.dequeue()

# Example usage
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Peek:", queue.peek())

queue.dequeue()
queue.dequeue()

print("Peek:", queue.peek())

queue.dequeue()
queue.dequeue() # Try to dequeue from empty queue

queue.free_queue() #Free all nodes.