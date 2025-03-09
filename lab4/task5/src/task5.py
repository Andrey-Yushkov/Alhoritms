from lab4.utils import file_read, file_write, measure

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def max(self):
        return self.max_stack[-1] if self.max_stack else None


def process_max_stack():
    commands = file_read()
    max_stack = Stack()
    results = []

    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            max_stack.push(int(value))
        elif command == "pop":
            max_stack.pop()
        elif command == "max":
            results.append(max_stack.max())

    file_write(results)

if __name__ == '__main__':
    measure(process_max_stack)