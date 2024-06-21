__doc__ = """
    
    Queue Class consist some mothods such as:

        is_empty()
        is_full()
        enqueue()
        dequeue()
        front()
"""

class Queue():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list_data = []

    def is_empty(self):
        return len(self.__list_data) == 0

    def is_full(self):
        return len(self.__list_data) == self.__capacity

    def enqueue(self, _data):
        if self.is_full():
            print("Queue is full")
        else:
            self.__list_data.append(_data)

    def  dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.__list_data.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.__list_data[0]

if __name__ =="__main__":
    
    queue1 = Queue (5)
    queue1.enqueue (1)
    queue1.enqueue (2)
    print (queue1.is_full())
    print (queue1.front())
    print (queue1.dequeue())
    print (queue1.front())
    print (queue1.dequeue())
    print (queue1.is_empty())