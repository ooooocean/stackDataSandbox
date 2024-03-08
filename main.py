"""
Playing around with stack data structure, using it to reverse letters.
"""


def create_stack(stack):
    stack = [x for x in str(stack)]
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


def reverse_stack(input):
    stack = create_stack(input)
    new_word = ''
    while stack_is_empty(stack) is False:
        new_word += pop_stack(stack)
    print(f'"{input}" was reversed to "{new_word}"')
    return new_word


def reverse_stack_with_recursion(stack, string):
    """This needs to take the input as a stack already for the recursion to work."""
    if stack:
        string += pop_stack(stack)
        reverse_stack_with_recursion(stack, string)
    else:
        return string
