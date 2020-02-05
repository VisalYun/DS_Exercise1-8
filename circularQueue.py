class CircularQueue():

    # constructor
    def __init__(self, size):  # initializing the class
        self.size = size

        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, input):

        # condition if queue is full
        if ((self.rear + 1) % self.size == self.front):
            print(" Queue is Full\n")

            # condition for empty queue
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = input
            print("Enqueue successfully")
        else:

            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = input
            print("Enqueue successfully")

    def dequeue(self):
        if (self.front == -1):  # codition for empty queue
            print("Queue is Empty\n")

            # condition for only one element
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            print("Dequeue successfully")
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print("Dequeue successfully")
            return temp

    def display(self):

        # condition for empty queue
        if (self.front == -1):
            print("Queue is Empty")

        elif (self.rear >= self.front):
            print("Elements in the circular queue are:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Elements in Circular Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")

    def overAndUnderFlow(self, size):
        if self.front == -1:
            print("~~Circular Queue Underflow~~")
        elif self.front == (self.rear + 1) % size:
            print("\n\n~~Circular Queue Overflow~~")
        else:
            print("No overflow or underflow")