# -----------------------------------------------------
# CSCI 127, Lab 8                                     |
# June 12, 2020                                       |
# Adam Wulfing                                        |
# -----------------------------------------------------

class Queue:
    def __init__(self, numbers):
        self.n = []
        
    def enqueue(self, numbers):
        self.n.append(numbers)
    
    def dequeue(self):
         return self.n.pop(0)
    
    def is_empty(self):
        return self.n == []

    def __str__(self):
        return "Contents: " + str(self.n)

    def __iadd__(self, num):
        self.n.append(num)

# -----------------------------------------------------

def main():
    numbers = Queue("Numbers")

    print("Enqueue 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item")
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.enqueue(number)

    # Enqueue 15
    numbers += 15

    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()
