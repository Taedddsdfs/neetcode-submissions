from collections import deque

class MyStack:

    def __init__(self):
        # Initialize an empty deque to store elements
        self.q = deque()

    def push(self, x: int) -> None:
        # Push the element to the back of the queue
        self.q.append(x)
        
        # Rotate the queue to bring the newly added element to the front
        # This simulates LIFO behavior using a FIFO structure
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # The front of the queue is the top of the stack
        return self.q.popleft()

    def top(self) -> int:
        # Return the element at the front without removing it
        return self.q[0]

    def empty(self) -> bool:
        # Returns True if the queue is empty, False otherwise
        return not self.q