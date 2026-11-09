class Stack:
    # init
    def __init__(self):
        self.items = []

    # push
    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    # is_empty
    def is_empty(self):
        if self.items:
            return False
        else:
            return True
    # pop
    def pop(self):
        return self.items.pop()

    # top
    def top(self):
        return self.items[-1]


N = int(input())


commands = [input() for _ in range(N)]

s = Stack()

for command in commands:
    if "h" in command:
        origin, num = command.split()
        s.push(int(num))
    elif command == "pop":
        print(s.pop())
    elif command == "size":
        print(s.size()) 
    elif command == "empty":
        print(1 if s.is_empty() else 0)
    elif command == "top":
        print(s.top())