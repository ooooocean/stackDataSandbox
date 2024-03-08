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
    if not stack:
        print(string)
        return(string)
    else:
        string += pop_stack(stack)
        reverse_stack_with_recursion(stack, string)


def reverse_individual_words_in_stack(words):
    words_stack = create_stack(words)
    new_words = []
    buffer_stack = []
    # iterate until the stack is empty
    while words_stack:
        # add letters to the new stack from our input
        print(f'Original Stack is {words_stack}')
        new_words.append(pop_stack(words_stack))
        print(f'New stack is {new_words}\n'
              f'Original stack is now {words_stack}.\n')
        # when a space is found, pop the stack to a buffer for later
        if peek_stack(words_stack) == ' ':
            # iterate through our new stack until it is empty
            while new_words:
                # pop the space from the new stack to retain word order
                pop_stack(new_words)
                # move words to buffer
                buffer_stack += pop_stack(new_words)
            # once input is empty, add a space to the top of the buffer stack to preserve spacing
            else:
                push_stack(buffer_stack, ' ')
    # once words have all been iterated through, add words back in from the buffer
    else:
        while buffer_stack:
            new_words.append(pop_stack(buffer_stack))
        # once buffer_stack is empty, print the new stack
        else:
            return new_words

print(reverse_individual_words_in_stack('Hello World'))
