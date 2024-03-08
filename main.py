"""
Playing around with stack data structure, using it to reverse letters.
"""


def create_text_stack(stack):
    stack = [x for x in stack]
    return stack


def stack_is_empty(stack):
    if not stack:
        return True
    else:
        return False


def pop_stack(stack):
    if stack_is_empty(stack):
        print('Stack is empty.')
    return stack.pop()


def push_stack(stack, item):
    stack.append(item)
    print(f'Pushed item: {item}')

