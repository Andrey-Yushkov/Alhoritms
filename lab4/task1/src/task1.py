from lab4.utils import file_read, file_write, measure


class Stack:
    def __init__(this):
        this.stack = []
    def push(this, value):
        this.stack.append(value)
    def pop(this):
        return this.stack.pop() if this.stack else None

def process_stack_commands(commands):
    stack = Stack()
    results = []

    for command in commands:
        if command.startswith('+'):
            _, value = command.split()
            stack.push(int(value))
        elif command == '-':
            results.append(stack.pop())

    return results


if __name__ == '__main__':
    commands = file_read()
    result = measure(process_stack_commands, commands)
    file_write(result[0])