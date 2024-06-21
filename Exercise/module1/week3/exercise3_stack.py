__doc__ = """
    
    Stack Class consist some mothods such as:

        is_empty()
        is_full()
        pop()
        push()
        top()
        
"""

class Stack():
    def __init__(self, capacity) :
        self.__capacity = capacity
        self.__list_data = []

    def is_empty(self):
        return len(self.__list_data) == 0

    def is_full(self):
        return len(self.__list_data) == self.__capacity

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.__list_data.pop()

    def push(self, _data):
        if self.is_full():
            print("Stack is full")
        else:
            self.__list_data.append(_data)

    def top(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.__list_data[-1]


if __name__ == "__main__":
    
    stack = Stack(5)
    print(stack.push(1))
    print(stack.push(2))
    print(stack.push(3))
    print(stack.push(4))

    print(stack.top())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.is_full())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())