# Stack implemented with a list and functions

stack = []

def push(item):
    stack.append(item)

def pop():
    if not is_empty():
        return stack.pop()
    return None

def peek():
    if not is_empty():
        return stack[-1]
    return None

def is_empty():
    return len(stack) == 0

# Example usage:
push(10)
push(20)
print(peek())  # Output: 20
print(pop())   # Output: 20
print(pop())   # Output: 10
print(pop())   # Output: None  (stack is empty)
